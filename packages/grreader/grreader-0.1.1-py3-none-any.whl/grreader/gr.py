import re
from textwrap import shorten

import requests
from bs4 import BeautifulSoup
from lxml import etree


def scrape_goodreads_image_url(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    img_url = soup.find(id='coverImage')
    if img_url:
        return img_url.get('src')
    try:
        img_url = soup.find(class_='BookCover').img.get('src')
    except AttributeError as err:
        e = err
        return
    return img_url


class GoodreadsXML:
    def __init__(self, xml):
        self.tree_init = etree.XML(xml)
        self.tree = etree.XML(xml)
        if self.tree.find('book') is not None:
            self.tree = self.tree.find('book')
        self.xml = xml

    def __bool__(self):
        return self.tree.find('id') is not None

    def __str__(self):
        t, a = self.title(), self.author()
        return f'{t} by {a}'

    def __repr__(self):
        t, a = self.title(), self.author()
        return f'{t} by {a} [{self.goodreads_id()}]'

    @classmethod
    def from_text(cls, text):
        xml = bytes(text, encoding="UTF-8")
        return cls(xml=xml)

    def tree_to_string(self):
        return etree.tostring(self.tree)

    def xml_text(self):
        return str(self.xml, encoding="UTF-8")

    def title(self):
        return self.tree.findtext('title', '')

    def author(self):
        return self.tree.findtext('authors/author/name', '')

    def title_author(self, short=False):
        t, a = self.title(), self.author()
        if short:
            t = shorten(t, 30)
            a = shorten(a, 20)
        return f'{t} - {a}'

    def goodreads_id(self):
        return self.tree.findtext('id')

    def average_rating(self):
        if self.tree.findtext('average_rating'):
            return float(self.tree.findtext('average_rating'))

    def ratings_count(self):
        if self.tree.findtext('work/ratings_count'):
            return int(self.tree.findtext('work/ratings_count'))

    def best_book_id(self):
        return self.tree.findtext('work/best_book_id')

    def description(self):
        return self.tree.findtext('description')

    def image_url(self):
        return self.tree.findtext('image_url')

    def image_url2(self):
        img = self.image_url() or 'nophoto'
        if 'nophoto' in img:
            img = scrape_goodreads_image_url(self.url())
        else:
            img = re.sub(r'\._[\w\d]+_', '', img)
        return img

    def scrape_image_url(self):
        return scrape_goodreads_image_url(self.url())

    def url(self):
        return self.tree.findtext('url')

    def publication_year(self):
        return self.tree.findtext('work/original_publication_year')

    def num_pages(self):
        return self.tree.findtext('num_pages')

    def reviews_widget(self):
        return self.tree.findtext('reviews_widget')

    def popular_shelves(self):
        pop_shelves = self.tree.find('popular_shelves') or []
        return [(s.get('name'), s.get('count')) for s in pop_shelves]

    def popular_shelves_normalized(self):
        shelf_dict = {}
        for s in self.popular_shelves():
            name, count = s
            new_name = name.replace('-', '')
            new_count = shelf_dict.get(new_name, 0) + int(count)
            shelf_dict[new_name] = new_count
        shelves = sorted(shelf_dict.items(), key=lambda x: x[1], reverse=True)
        return shelves

    def similar_books(self):
        similar_books = self.tree.find('similar_books') or []
        book_items = [etree.tostring(b) for b in similar_books.iterchildren()]
        gr_xmls = [GoodreadsXML(b) for b in book_items]
        return gr_xmls

    def is_best_book_id(self):
        if self.goodreads_id() and self.best_book_id():
            return self.goodreads_id() == self.best_book_id()

    def isbns(self):
        isbns = [
            self.tree.findtext('isbn'),
            self.tree.findtext('isbn13')
        ]
        return [isbn for isbn in isbns if isbn]

    def ratings_dist_list(self):
        dist = self.tree.findtext('work/rating_dist')
        if not dist:
            return
        dist_dict = dict([tuple(x.split(':')) for x in dist.split('|')])
        total_ratings = dist_dict.get('total', '0')
        total_ratings = int(total_ratings)
        result = []
        for i in range(5, 0, -1):
            count = int(dist_dict.get(str(i)))
            count_pct = count / max(total_ratings, 1)
            result.append((i, count, count_pct))
        return result

    def ratings_dist_dict(self):
        d = {}
        for i, cnt, pct in self.ratings_dist_list():
            k = f'ratings_count{i}'
            d[k] = cnt
            k2 = k + '_pct'
            d[k2] = int(100 * pct)
        return d

    def dict_for_db(self):
        data = dict(
            author=self.author(),
            average_rating=self.average_rating(),
            best_book_id=self.best_book_id(),
            description=self.description(),
            goodreads_id=self.goodreads_id(),
            image_url=self.image_url2(),
            ratings_count=self.ratings_count(),
            title=self.title(),
            url=self.url(),
            publication_year=self.publication_year(),
            num_pages=self.num_pages(),
            **self.ratings_dist_dict(),
        )
        return data


class GoodreadsClient:
    url_by_id = 'https://www.goodreads.com/book/show.xml'
    url_by_title = 'https://www.goodreads.com/book/title.xml'
    reviews_url = 'https://www.goodreads.com/book/review_counts.json'
    search_url = 'https://www.goodreads.com/search/index.xml'
    url_by_isbn = 'https://www.goodreads.com/book/isbn'
    list_shelves = 'https://www.goodreads.com/shelf/list.xml?key=E4AuxnmOm4k01jQPJn9RJw'

    def __init__(self, api_key):
        self.api_key = api_key
        self.history = []

    @property
    def last_request(self):
        if self.history:
            return self.history[-1]

    def _get_response(self, url, params):
        resp, err = None, None
        try:
            resp = requests.get(url, params=params, allow_redirects=False, timeout=6.0)
            req = resp.request
        except requests.RequestException as e:
            print(e)
            err = e
            req = e.request
        self.history.append(dict(request=req, response=resp, error=err))

        if resp and resp.ok:
            return GoodreadsXML(xml=resp.content)

    def get_url(self, goodreads_id=None, title=None, author=None, isbn=None):
        params = {'key': self.api_key}
        if goodreads_id:
            url = self.url_by_id
            params['id'] = goodreads_id
        elif isbn:
            url = self.url_by_isbn
            params = {'isbn': isbn}
        else:
            url = self.url_by_title
            params.update(dict(title=title, author=author))
        return url, params

    def get_book(self, goodreads_id=None, title=None, author=None, isbn=None):
        url, params = self.get_url(goodreads_id=goodreads_id, title=title, author=author, isbn=isbn)
        return self._get_response(url, params)

    def search(self, title, author=None):
        url, params = self.get_url(title=title, author=author)
        gr = self._get_response(url, params)
        return gr

    def from_goodreads_id(self, goodreads_id):
        url, params = self.get_url(goodreads_id=goodreads_id)
        gr = self._get_response(url, params)
        return gr

    def from_isbn(self, isbn):
        url, params = self.get_url(isbn=isbn)
        gr = self._get_response(url, params)
        return gr

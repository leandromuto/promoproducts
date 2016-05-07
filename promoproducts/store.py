# -*- coding: utf-8 -*-

import urllib

import re
from bs4 import BeautifulSoup
from promoproducts import Promoproducts


class Store(object):
    def __init__(self, store):
        self.encoding = Promoproducts().encoding
        self.stores = Promoproducts().get_stores()

        self.store = store

        self.departments = [
            'Beleza e Saúde', 'Brinquedos',
            'Cama, Mesa e Banho', 'Eletrodomésticos',
            'Eletroportáteis', 'Esporte e Lazer', 'Games',
            'Informática', 'Livros', 'Tablets',
            'Telefones e Celulares', 'TV e Vídeo',
            'Telefonia', 'Eletrônicos'
        ]

    def call_me(self):

        store_prods = []

        # retorna uma list de dicts com todos os departamentos
        depts = self.get_departments(self.store, [])

        print(depts)

        if not depts:
            return []

        for d in depts:
            d['department_categories'] = self.get_categories(
                d['department_href'])

            print(d['department_href'])

            for c in d['department_categories']:
                c['category_products'] = self.get_products(c['category_href'])

            print(d)

        return store_prods

    def get_departments(self):
        depts = []

        # HTML of coupons page
        html = urllib.urlopen(self.store).read()

        # making a soup
        soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)
        departments_link = soup.select(self.depto_css)

        for d in departments_link:
            if d.text.encode('utf8') in self.departments:
                depts.append({
                    'department_name': d.text.encode('utf8'),
                    'department_href': d['href']
                })

        return depts

    def get_categories(self, depto):
        """
        Get all categories from Extra departments.
        E.g. Bonecos, Playground etc from Brinquedos

        Args:
            :param depto: (str) a link to department link

        Return:
            :return:
        """

        categories = []

        # HTML of department page
        html = urllib.urlopen(depto).read()

        # making a soup
        soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)

        # all categories available
        categories_link = soup.select(self.category_css)

        for c in categories_link:
            categories.append({
                'category_name': c.text.encode('utf8'),
                'category_href': c['href']
            })

        return categories

    def get_products(self, category):
        """
        Get all products from one category.

        Param:
            :param category: (str) a link to the category from department
            :param product: (str) the CSS of product wrapper
            :param from_price: (str) the CSS of normal price of product
            :param on_sale: (str) the CSS of on sale price of product
            :param next_page: (str) the CSS of next page link

        Return:
            :return: Returns a list of products informations
        """

        first_time = True

        # just for loop works for the first time
        next_page = True

        products = []

        while next_page:

            if first_time:
                # HTML of category page
                html = urllib.urlopen(category).read()

                first_time = False
            else:
                # HTML of category page
                html = urllib.urlopen(category_next_page).read()

            # making a soup
            soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)

            # prods from page
            ps = soup.select(self.product_css)

            # infos of single prod
            for p in ps:
                # if prod is available then will be 1
                available = 1

                # prod price
                from_price = p.find('span', attrs={'class': 'from price regular'})
                on_sale = p.find('span', attrs={'class': 'for price sale'})

                if on_sale is None:
                    os = 0
                    available = 0  # when the product is not available
                else:
                    os = re.findall(r'([0-9]+\W+[0-9].)',
                                    str(on_sale).replace(',', '.'))[0]

                if from_price is None:
                    fp = os
                else:
                    fp = re.findall(r'([0-9]+\W+[0-9].)',
                                    str(from_price).replace(',', '.'))[0]

                # all info of prod together
                prod = {
                    'product_name': p.a['title'],
                    'product_img': p.span.img['data-src'],
                    'product_href': p.a['href'],
                    'product_from_price': float(fp),
                    'product_on_sale': float(os),
                    'product_available': available,
                }

                products.append(prod)

                category_next_page = soup.select(self.category_next_page_css)

                if category_next_page:
                    category_next_page = category_next_page[0]['href']
                else:
                    next_page = False

        return products

class Extra(Store):
    def __init__(self, store=None, depto_css=None, category_css=None,
                 category_next_page_css=None,
                 product_css=None):
        self.store = store or 'http://www.extra.com.br/'
        super(Extra, self).__init__(self.store)

        self.depto_css = depto_css or 'li.nav-item-todos li.navsub-item a'
        self.category_css = category_css or 'div.navigation h3.tit > a'
        self.category_next_page_css = category_next_page_css or 'div.pagination li.next > a'
        self.product_css = product_css or 'div.lista-produto div.hproduct'


class PontoFrio(Store):
    def __init__(self, store=None, depto_css=None, category_css=None,
                 category_next_page_css=None,
                 product_css=None):
        self.store = store or 'http://www.pontofrio.com.br/'
        super(PontoFrio, self).__init__(self.store)

        self.depto_css = depto_css or 'li.todasCategorias li.it-sbmn > a'
        self.category_css = category_css or 'div.navigation h3.tit > a'
        self.category_next_page_css = category_next_page_css or 'div.pagination li.next > a'
        self.product_css = product_css or 'div.lista-produto div.hproduct'


class RicardoEletro(Store):
    def call_me(self):
        super(RicardoEletro, self).call_me()

    def get_departments(self):
        return super(RicardoEletro, self).get_departments(self.depto_css)

    def get_categories(self):
        return super(RicardoEletro, self).get_categories(self.depto_css,
                                                         self.category_css)

    def get_products(self):
        return super(RicardoEletro, self).get_products(self.category_css,
                                                       self.product_css)

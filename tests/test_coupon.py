"""This module contains an object that represents Tests for Coupon class"""

import sys
import unittest

sys.path.append('.')

from promoproducts.coupon import Coupon
from promoproducts.store import Store, Extra, PontoFrio, RicardoEletro

class CouponTest(unittest.TestCase):
    """This object represents Tests for Coupon class"""

    def test_new_coupon(self):
        coupon = Coupon()

        self.assertTrue(isinstance(coupon.valid_coupons, list))
        self.assertTrue(isinstance(coupon.stores, list))

        self.assertTrue("ponto-frio" in coupon.stores)

class ExtraTest(unittest.TestCase):

    def test_get_departments(self):
        extra = Extra()
        departments = extra.get_departments()

        self.assertEqual(departments[0]['department_name'],
                         'Beleza e Sa\xc3\xbade')

    def test_get_categories(self):
        extra = Extra()
        departments = extra.get_departments()
        category = extra.get_categories(departments[0])

        self.assertEqual(category[0]['category_href'],
                         'http://www.extra.com.br/BelezaSaude/cuidadosfemininos/?Filtro=C102_C105')

        self.assertEqual(category[0]['category_name'],
                         'Cuidados Femininos')

    # def test_get_products(self):
    #     store = Extra()
    #     departments = store.get_departments()
    #     category = store.get_categories(departments[0]['department_href'])
    #     products = store.get_products(category[0]['category_href'])
    #
    #     self.assertIsInstance(products[0]['product_from_price'], float)
    #     self.assertIsInstance(products[0]['product_available'], int)
    #     self.assertEqual(products[0]['product_href'], u'http://www.extra.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.html?recsource=busca-int&rectype=busca-105')
    #     self.assertIsInstance(products[0]['product_on_sale'], float)
    #     self.assertEqual(products[0]['product_name'], u'Escova Rotativa Philco Spin Brush 55401001 - Preta/Vermelha')
    #     self.assertEqual(products[0]['product_img'], u'http://www.extra-imagens.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/1654285/6749539/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.jpg')

class PontoFrioTest(unittest.TestCase):

    def test_get_departments(self):
        pf = PontoFrio()
        departments = pf.get_departments()

        self.assertEqual(departments[0]['department_name'],
                         'Beleza e Sa\xc3\xbade')

    # def test_get_categories(self):
    #     pf = PontoFrio()
    #     departments = pf.get_departments()
    #     category = pf.get_categories(departments[0]['department_href'])
    #
    #
    #     self.assertEqual(category[0]['category_href'],
    #                      'http://www.pontofrio.com.br/BelezaSaude/cuidadosfemininos/?Filtro=C102_C105')
    #
    #     self.assertEqual(category[0]['category_name'],
    #                      'Cuidados Femininos')
    #
    # def test_get_products(self):
    #     pf = PontoFrio()
    #     departments = pf.get_departments()
    #     category = pf.get_categories(departments[0]['department_href'])
    #     products = pf.get_products(category[0]['category_href'])
    #
    #     self.assertIsInstance(products[0]['product_from_price'], float)
    #     self.assertIsInstance(products[0]['product_available'], int)
    #     self.assertEqual(products[0]['product_href'],
    #                      u'http://www.pontofrio.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.html?recsource=busca-int&rectype=busca-105')
    #     self.assertIsInstance(products[0]['product_on_sale'], float)
    #     self.assertEqual(products[0]['product_name'], u'Escova Rotativa Philco Spin Brush 55401001 - Preta/Vermelha')
    #     self.assertEqual(products[0]['product_img'],
    #                      u'http://www.pontofrio-imagens.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/1654285/6749539/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.jpg')

# class RicardoEletro(unittest.TestCase):
#
#     def test_get_departments(self):
#         re = RicardoEletro('http://www.ricardoeletro.com.br/')
#         departments = re.get_departments('div.CategoriasHeader div.loja > a')
#
#         self.assertEqual(departments[0]['department_name'],
#                          'Beleza e Sa\xc3\xbade')
#
    # def test_get_categories(self):
    #     re = RicardoEletro('http://www.ricardoeletro.com.br')
    #     departments = w.get_departments('li.todasCategorias li.it-sbmn > a')
    #     category = w.get_categories(departments[0]['department_href'], 'div.navigation h3.tit > a')
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(category[0]['category_href'],
    #                      'http://www.walmart.com.br/BelezaSaude/cuidadosfemininos/?Filtro=C102_C105')
    #
    #     self.assertEqual(category[0]['category_name'],
    #                      'Cuidados Femininos')
    #
    # def test_get_products(self):
    #     re = RicardoEletro('http://www.ricardoeletro.com.br')
    #     departments = w.get_departments('li.todo-shopping li.it-sbmn > a')
    #     category = w.get_categories(departments[0]['department_href'], 'div.navigation h3.tit > a')
    #     products = w.get_products(category[0]['category_href'], 'div.lista-produto div.hproduct')
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(products[0]['product_from_price'], u'R$ 155,00')
    #     self.assertEqual(products[0]['product_available'], 1)
    #     self.assertEqual(products[0]['product_href'],
    #                      u'http://www.pontofrio.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.html?recsource=busca-int&rectype=busca-105')
    #     self.assertEqual(products[0]['product_on_sale'], u'R$ 105,90')
    #     self.assertEqual(products[0]['product_name'], u'Escova Rotativa Philco Spin Brush 55401001 - Preta/Vermelha')
    #     self.assertEqual(products[0]['product_img'],
    #                      u'http://www.pontofrio-imagens.com.br/BelezaSaude/cuidadosfemininos/modelaroreseescovasrotativas/1654285/6749539/Escova-Rotativa-Philco-Spin-Brush-55401001-Preta-Vermelha-1654285.jpg')


if __name__ == '__main__':
    unittest.main()

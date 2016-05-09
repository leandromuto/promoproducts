import urllib
import time
from bs4 import BeautifulSoup
from promoproducts import Promoproducts

import django
import os
import sys
sys.path.append('../promosite')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "promosite.settings")
django.setup()

from promosite.models import *

class Coupon(object):
    def __init__(self):
        self.valid_coupons = []
        self.stores = Promoproducts().get_stores()

    def coupon_url(self, store):
        """
        Method to generate coupon website for specific store

        Args:
            :param store: (string) Store name

        Return:
            :return: Returns the url of coupon website
        """

        # Base of URL of coupons page
        base_url = 'http://blog.thiagorodrigo.com.br/cupom-desconto-'
        url = base_url + store

        return url

    def get_coupons(self):
        """
        Method to get coupons from website

        Return:
            :return: Returns an array of valid coupons after search for them in website
        """

        for store in self.stores:
            url = self.coupon_url(store)

            # HTML of coupons page
            html = urllib.urlopen(url).read()

            # making a soup
            soup = BeautifulSoup(html)

            # get coupons
            coupons = soup.select('ul.vt-skin-green li.vt-line div.vt-content')

            for coupon in coupons:
                # coupon's code
                cod = coupon.find_all('a', attrs={'data-cupom': True})

                if cod:
                    val = {
                            'coupon_code': cod[0]['data-cupom'],
                            'coupon_store': store,
                            'time': time.strftime("%x")
                          }
                    self.valid_coupons.append(dict(val))
                    ModelCoupon.get_or_create(ModelCoupon.coupon_code==val['coupon_code'])

        return self.valid_coupons

    def all_coupons(self):
        """
        Get all cupons from valid_coupons variable.

        Return:
            :return: Returns a list of cupons. If valid_coupon is empty, then returns none.
        """
        if self.valid_coupons:
            return self.valid_coupons
        else:
            return

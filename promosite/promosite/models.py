from django.db import models


class Store(models.Model):
    store_name = models.CharField(max_length=255, unique=True)
    store_href = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.store_name


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_href = models.CharField(max_length=255, unique=True)
    department_store = models.ForeignKey(Store)

    def __unicode__(self):
        return self.department_name


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_href = models.CharField(max_length=255, unique=True)
    category_department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_img = models.CharField(max_length=255)
    product_href = models.CharField(max_length=255, unique=True)
    product_from_price = models.FloatField()
    product_on_sale = models.FloatField()
    product_is_available = models.IntegerField()
    product_category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.product_name


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=255)
    coupon_store = models.ForeignKey(Store)

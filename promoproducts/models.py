from peewee import *

db = SqliteDatabase('promo.db')

class Store(Model):
    id = PrimaryKeyField()
    name = CharField()
    url = CharField()

class Department(Model):
    name = CharField()
    url = CharField()
    stores = ForeignKeyField(Store)

class Category(Model):
    name = CharField()
    url = CharField()
    departments = ForeignKeyField(Department)

class Product(Model):
    name = CharField()
    img_url = CharField()
    url = CharField()
    from_price = FloatField()
    on_sale = FloatField()
    is_available = IntegerField()
    categories = ForeignKeyField(Category)

class Coupon(Model):
    id = PrimaryKeyField()
    codigo = CharField()
    stores = ForeignKeyField(Store)

def create_tables():
    db.connect()
    db.create_tables([Store, Department, Category, Product, Coupon])

import pdb; pdb.set_trace()
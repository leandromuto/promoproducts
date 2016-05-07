from peewee import *

db = SqliteDatabase('promo.db')


class Store(Model):
    id = PrimaryKeyField(unique=True)
    store_name = CharField(unique=True)
    store_href = CharField(unique=True)


class Department(Model):
    id = PrimaryKeyField(unique=True)
    department_name = CharField()
    department_href = CharField()
    store = ForeignKeyField(Store)


class Category(Model):
    id = PrimaryKeyField(unique=True)
    category_name = CharField()
    category_href = CharField()
    departments = ForeignKeyField(Department)


class Product(Model):
    id = PrimaryKeyField(unique=True)
    product_name = CharField()
    product_img_url = CharField()
    product_url = CharField()
    product_from_price = FloatField()
    product_on_sale = FloatField()
    product_is_available = IntegerField()
    product_categories = ForeignKeyField(Category)


class Coupon(Model):
    id = PrimaryKeyField(unique=True)
    coupon_code = CharField()
    coupon_store = ForeignKeyField(Store)


def create_tables():
    db.connect()
    db.create_tables([Store, Department, Category, Product, Coupon])


if __name__ == '__main__':
    create_tables()

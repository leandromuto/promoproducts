from peewee import *

db = SqliteDatabase('promo.db')


class Store(Model):
    id = PrimaryKeyField(unique=True)
    store_name = CharField(unique=True)
    store_href = CharField(unique=True)

    class Meta:
        database = db


class Department(Model):
    id = PrimaryKeyField(unique=True)
    department_name = CharField()
    department_href = CharField()
    department_store = ForeignKeyField(Store)


    class Meta:
        database = db


class Category(Model):
    id = PrimaryKeyField(unique=True)
    category_name = CharField()
    category_href = CharField()
    category_department = ForeignKeyField(Department)

    class Meta:
        database = db


class Product(Model):
    id = PrimaryKeyField(unique=True)
    product_name = CharField()
    product_img = CharField()
    product_href = CharField()
    product_from_price = FloatField()
    product_on_sale = FloatField()
    product_is_available = IntegerField()
    product_category = ForeignKeyField(Category)

    class Meta:
        database = db


class Coupon(Model):
    id = PrimaryKeyField(unique=True)
    coupon_code = CharField()
    coupon_store = ForeignKeyField(Store)

    class Meta:
        database = db


def create_tables():
    db.connect()
    db.create_tables([Store, Department, Category, Product, Coupon])


if __name__ == '__main__':
    create_tables()

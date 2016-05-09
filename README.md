=============
promoproducts
=============

----------
Setting Up
----------

Clone this repository:

```
$ git clone https://github.com/leandromuto/promoproducts.git
$ cd promoproducts
```

Assuming you have `virtualenv` and `pip` installed:

```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Getting start with Django:

```
$ python promosite/manage.py migrate
$ python promosite/manage.py makemigrations promosite
$ python promosite/manage.py migrate
$ python promosite/manage.py createsuperuser
$ python promosite/manage.py runserver
```

To run tests:

```
$ nosetests
```
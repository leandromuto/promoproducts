# middleware.py
from my_blog.db import database  # Import the peewee database instance.


class PeeweeConnectionMiddleware(object):
    def process_request(self, request):
        database.connect()

    def process_response(self, request, response):
        if not database.is_closed():
            database.close()
        return response
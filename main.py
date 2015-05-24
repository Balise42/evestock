# Stdlib
import logging
import os

# Libraries
import webapp2
import jinja2

# S.H.M
from stock import Stock
from config import error_action

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stock = Stock()
        bookquantities = sorted(
            stock.list_of_items,
            key=lambda quantity: quantity['class']+quantity['name'])
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({'bookquantities': bookquantities}))

    def handle_exception(self, exception, debug_mode):
        logging.exception("Exception thrown:")
        template = JINJA_ENVIRONMENT.get_template('error.html')
        self.response.write(template.render({'action': error_action}))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

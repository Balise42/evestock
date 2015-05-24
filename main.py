# Stdlib
import logging
import os

# Libraries
import webapp2
import jinja2

# S.H.M
from stock import Stock
from common import sheet
from config import description, error_action
from util import setup_logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stock = Stock()
        template = JINJA_ENVIRONMENT.get_template('index.html')
        data = {
            'corpTicker': sheet['ticker'],
            'report': stock.build_report(),
            'description': description,
        }
        self.response.write(template.render(data))

    def handle_exception(self, exception, debug_mode):
        logging.exception("Exception thrown:")
        template = JINJA_ENVIRONMENT.get_template('error.html')
        self.response.write(template.render({'action': error_action}))

setup_logging()
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

import webapp2
import evelink

from keys import keyid, vcode
from config import sysid

class MainHandler(webapp2.RequestHandler):
    eve = evelink.eve.EVE()
    vn = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))
    assets = vn.assets()



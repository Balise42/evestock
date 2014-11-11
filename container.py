import evelink
withmemcache = True
try:
    from google.appengine.api import memcache
except ImportError:
    withmemcache = False

from keys import keyid, vcode

class Container:
  def __init__(self, containername):
    self.containername = containername
    self.eve = evelink.eve.EVE()
    self.vn = evelink.corp.Corp(evelink.API(api_key = (keyid, vcode)))

    

import evelink
withmemcache = True
try:
  from google.appengine.api import memcache
except ImportError:
  withmemcache = False

from keys import keyid, vcode

class Station:
  def __init__(self, stationname):
    self.stationname = stationname
    self.eve = evelink.eve.EVE()
    self.corp = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

  def fetch_station_id(self):
    if withmemcache:
      self.fetch_station_id_from_cache()
      if(self.stationid is None):
        self.stationid = self.fetch_station_id_from_api()
        self.store_station_id_in_cache()
    else:
      self.fetch_station_id_from_api()
        
      
  def fetch_station_id_from_api(self):
    stations = self.eve.conquerable_stations().result
    for stationid, station in stations.iteritem():
      if station["name"] == self.stationnname:
        self.stationid = stationid+6000000

  def fetch_station_id_from_cache(self):
    self.stationid = memcache.get("stationid")

  def store_station_id_in_cache(self):
    memcache.add("stationid", self.stationid)


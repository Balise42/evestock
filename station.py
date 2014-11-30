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
    self.office = None
    self.corp = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

  def fetch_station_id(self):
    if withmemcache:
      self.fetch_station_id_from_cache()
      if(self.stationid is None):
        self.stationid = self.fetch_station_id_from_api()
        self.store_station_id_in_cache()
    else:
      self.fetch_station_id_from_api()
        
  def get_all_container_ids(self):
    self.fetch_assets()
    containerids = self.list_asset_if_container()
    return containerids

  def list_asset_if_container(self):
    containerids = []
    for asset in self.assets:
      if self.is_container(asset):
        containerids.append(asset["id"])

  def is_container(self, asset):
    return "contents" in asset
    
  def fetch_assets(self):
    self.fetch_office_if_none()
    self.assets = self.office["contents"]
    return self.assets

  def fetch_office_if_none(self):
    if self.office is None:
      stationid = self.stationid
      self.office = self.corp.assets().result[stationid]["contents"][0]
 
  def get_content_from_container(self, containerid):
    assets = self.fetch_assets()
    for asset in assets:
      if asset['id'] == containerid and is_container(asset['id']):
        return asset['contents']
    raise Exception('Could not find the container contents')
    
  #TODO add code for non-conquerable stations
  def fetch_station_id_from_api(self):
    stations = self.eve.conquerable_stations().result
    for stationid, station in stations.iteritems():
      if station["name"] == self.stationname:
        self.stationid = stationid+6000000

  def fetch_station_id_from_cache(self):
    self.stationid = memcache.get("stationid")

  def store_station_id_in_cache(self):
    memcache.add("stationid", self.stationid)


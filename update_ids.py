import evelink
import logging
withmemcache = True
try:
    from google.appengine.api import memcache
except ImportError:
    withmemcache = False

from keys import keyid, vcode
from config import stationname, containername
from station import Station
from container import Container

eve = evelink.eve.EVE()
vn = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

def get_container_id():
  station = Station(stationname)
  station.fetch_station_id()
  container = Container(containername, station)
  container.fetch_container_id()
  return container.containerid

def get_station_id():
  station = Station(stationname)
  return station.stationid

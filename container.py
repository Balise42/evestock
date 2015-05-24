import evelink

withmemcache = True
try:
    from google.appengine.api import memcache
except ImportError:
    withmemcache = False

from quantities import Quantities
from keys import keyid, vcode


class Container:
    def __init__(self, containername, station):
        self.containername = containername
        self.station = station
        self.eve = evelink.eve.EVE()
        self.corp = evelink.corp.Corp(evelink.api.API(api_key=(keyid, vcode)))
        self.fetch_container_id()
        self.fetch_contents()
        self.fetch_quantities()

    def fetch_contents(self):
        self.station.fetch_assets()
        self.contents = self.station.get_content_from_container(
            self.containerid)

    def fetch_container_id(self):
        if withmemcache:
            self.fetch_container_id_from_cache()
            if(self.containerid is None):
                self.fetch_container_id_from_api()
                self.store_container_id_in_cache()
            else:
                self.fetch_container_id_from_api()

    def fetch_container_id_from_cache(self):
        self.containerid = memcache.get("containerid")

    def store_container_id_in_cache(self):
        memcache.add("containerid", self.containerid)

    def fetch_quantities(self):
        self.quantities = Quantities()
        for item in self.contents:
            self.quantities.add(item["item_type_id"], item["quantity"])

    def fetch_container_id_from_api(self):
        containerids = self.station.containerids
        if containerids is None:
            raise Exception('Could not fetch container ids')
        locations = self.corp.locations(containerids).result
        for idlocation, location in locations.iteritems():
            if location['name'] == self.containername:
                self.containerid = idlocation
        if self.containerid is None:
            raise Exception('Could not fetch the container id.')

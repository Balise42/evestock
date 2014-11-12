import evelink

from keys import keyid, vcode

class Container:
  def __init__(self, containername, station):
    self.containername = containername
    self.station = station
    self.eve = evelink.eve.EVE()
    self.corp = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))
    self.fetch_contents()

  def fetch_contents(self):
    self.fetch_container_id()
    if self.containerid is None:
      raise('Nope nope nope')


  def fetch_container_id(self):
    containerids = self.get_all_container_ids_from_station()
    locations = self.corp.locations(containerids).result
    for idlocation, location in locations.iteritems():
      if location['name'] == self.containername:
        self.containerid = idlocation


  def get_all_container_ids_from_station(self):
    office = self.get_office_from_station()
    assets = office["contents"]
    containerids = self.list_asset_if_container(assets)
    return containerids

  def get_office_from_station(self):
    stationid = self.station.stationid
    office = self.corp.assets().result[stationid]["contents"][0]
    return office

  def list_asset_if_container(self,assets):
    containerids = []
    for asset in assets:
      if "contents" in asset:
        containerids.append(asset["id"])
    return containerids

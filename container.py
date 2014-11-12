import evelink

from keys import keyid, vcode

class Container:
  def __init__(self, containername, station):
    self.containername = containername
    self.eve = evelink.eve.EVE()
    self.corp = evelink.corp.Corp(evelink.API(api_key = (keyid, vcode)))
    container.fetch_container_id()

  def fetch_container_id(self):
    containerids = get_container_ids()
    locations = corp.locations(ids).result
    for idlocation, location in locations.iteritems():
      if location['name'] == self.containername:
        self.containerid = idlocation
        break

  def get_all_container_ids_from_station():
    office = get_office_from_station()
    assets = office["contents"]
    containerids = list_asset_if_container(assets)
    return containerids

  def get_office_from_station():
    stationid = station.stationid
    office = self.corp.assets().result[stationid]["contents"][0]
    return office

  def list_asset_if_container(assets):
    containerids = []
    for asset in assets:
      if "contents" in asset:
        containerids.append(asset["id"])
    return containerids

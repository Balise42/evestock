import evelink
withmemcache = True
try:
  from google.appengine.api import memcache
except ImportError:
  withmemcache = False

from keys import keyid, vcode
from config import containername, dbname, booklist, bookids, allitems, stationname
from container import Container
from station import Station

# Gets the stock of the configured container in the configured station
# and compares it to the list of items that we want to track
class Stock:
  def __init__(self):
    self.station = Station(stationname)
    self.container = Container(containername, self.station)
    self.compute_stock()

  def compute_stock(self):
    self.quantities = self.container.quantities
    self.get_item_ids_from_db_dump()
    self.compute_stock_from_list()

  def compute_stock_from_list(self):
    self.get_items_from_list_quantities()
    if(allitems):
      self.get_items_not_in_list_quantities()

  def get_item_from_list_quantities(self):
    booknames = [s.strip() for s in open(booklist)]

    self.itemquantities = []
    for name in booknames:
        quant = {}
        quant["name"] = name
        if not name in self.items:
            quant["class"] = 'text-warning'
            quant["quantity"] = 'ERROR'
        elif self.quantities.contains_item(self.items[name]):
            quant["quantity"] = self.quantities.get_quantity(self.items[name])
            if self.quantities.get_quantity(self.items[name]) < 10:
                quant["class"] = 'text-danger'
            else:
                quant["class"] = 'text-info'
        else:
            quant["quantity"] = 0
            quant["class"] = 'text-danger'
        self.itemquantities.append(quant)

  def get_items_not_in_list_quantities(self):
    if(allitems):
        for item in self.container.contents:
            if not self.itemsbyid[item["item_type_id"]] in booknames:
                quant = {}
                quant["name"] = self.itemsbyid[item["item_type_id"]]
                quant["class"] = 'text-warning'
                quant["quantity"] = self.quantities[item["item_type_id"]]
                self.itemquantities.append(quant)

  def get_item_ids_from_db_dump(self):
    lines = [s.strip() for s in open(bookids)]
    self.items = {}
    self.itemsbyid = {}
    for line in lines:
        [id, name] = line.split(' ', 1)
        self.items[name] = int(id)
        self.itemsbyid[int(id)] = name
 

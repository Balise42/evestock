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

class Stock:
  def __init__(self):
    self.station = Station(stationname)
    self.container = Container(containername, self.station)
    self.quantities = self.container.quantities
    self.get_item_ids_from_db_dump()
    self.compute_list_of_contents()

  def compute_list_of_contents(self):
    booknames = [s.strip() for s in open(booklist)]

    bookquantities = []
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
        bookquantities.append(quant)

    if(allitems):
        for skillbook in self.container.contents:
            if not self.itemsbyid[skillbook["item_type_id"]] in booknames:
                quant = {}
                quant["name"] = self.itemsbyid[skillbook["item_type_id"]]
                quant["class"] = 'text-warning'
                quant["quantity"] = self.quantities[skillbook["item_type_id"]]
                bookquantities.append(quant)
    self.list_of_items = bookquantities

  def get_item_ids_from_db_dump(self):
    lines = [s.strip() for s in open(bookids)]
    self.items = {}
    self.itemsbyid = {}
    for line in lines:
        [id, name] = line.split(' ', 1)
        self.items[name] = int(id)
        self.itemsbyid[int(id)] = name
 

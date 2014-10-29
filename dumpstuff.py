#!/usr/bin/python
import evelink
import pprint
import sqlite3

from keys import keyid, vcode
from config import stationid, smallcontainerid, dbname, booklist
eve = evelink.eve.EVE()
vn = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

pp = pprint.PrettyPrinter(indent=2)

assets = vn.assets()[stationid]["contents"][0]["contents"]

for asset in assets:
    if asset['id'] == smallcontainerid:
        skillbooks = asset['contents']

quantities = {}

for skillbook in skillbooks:
    quantities[skillbook["item_type_id"]] = skillbook["quantity"]

conn = sqlite3.connect(dbname)
conn.text_factory = str
c = conn.cursor()
items = {}
c.execute("SELECT typeId, typeName from invTypes")
for(itemid, name) in c:
    items[name] = itemid

booknames = [s.strip() for s in open(booklist)]
for name in booknames:
    if not name in items:
        print name, "ERROR"
    elif items[name] in quantities:
        print name, quantities[items[name]]
    else:
        print name, 0

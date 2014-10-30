import evelink
import sqlite3

from keys import keyid, vcode
from config import stationid, smallcontainerid, dbname, booklist

eve = evelink.eve.EVE()
vn = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

# containers are in station -> content -> office -> contents
assets = vn.assets()[stationid]["contents"][0]["contents"]

def get_item_ids_from_db():
    conn = sqlite3.connect(dbname)
    conn.text_factory = str
    c = conn.cursor()
    items = {}
    c.execute("SELECT typeId, typeName from invTypes")
    for(itemid, name) in c:
        items[name] = itemid
    return items

def get_quantities():
    # find the container
    for asset in assets:
        if asset['id'] == smallcontainerid:
            skillbooks = asset['contents']

    # enumerate the container with the items that are in it
    quantities = {}
    for skillbook in skillbooks:
        quantities[skillbook["item_type_id"]] = skillbook["quantity"]
    
    #get list of id/items matchings from DB
    items = get_item_ids_from_db()

    #get items we're interested in from file
    booknames = [s.strip() for s in open(booklist)]

    bookquantities = {}
    for name in booknames:
        bookquantities[name] = {}
        if not name in items:
            bookquantities[name]["class"] = 'text-warning'
            bookquantities[name]["quantity"] = 'ERROR'
        elif items[name] in quantities:
            bookquantities[name]["quantity"] = quantities[items[name]]
            if quantities[items[name]] < 10:
                bookquantities[name]["class"] = 'text-error'
            else:
                bookquantities[name]["class"] = 'text-info'
        else:
            bookquantities[name]["quantity"] = 0
            bookquantities[name]["class"] = 'text-error'

    return bookquantities

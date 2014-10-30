import evelink

from keys import keyid, vcode
from config import stationid, containername, dbname, booklist, bookids

eve = evelink.eve.EVE()
vn = evelink.corp.Corp(evelink.api.API(api_key = (keyid, vcode)))

assets = vn.assets().result[stationid]["contents"][0]["contents"]

def get_item_ids_from_db_dump():
    lines = [s.strip() for s in open(bookids)]
    items = {}
    itemsbyid = {}
    for line in lines:
        [id, name] = line.split(' ', 1)
        items[name] = int(id)
        itemsbyid[int(id)] = name
    return items, itemsbyid

def get_container():
    # containers are in station -> content -> office -> contents
    ids = []
    for asset in assets:
        # to check if an asset is a container which we can access,
        # we simply check if it has contents
        if "contents" in asset:
            ids.append(asset["id"])

        
    # and then we go through the Locations to find the right one
    locs = vn.locations(ids).result
    for id, loc in locs.iteritems():
        if loc['name'] == containername:
            for asset in assets:
                if asset['id'] == id:
                    return asset['contents']


def get_quantities(allitems):
    skillbooks = get_container()

    # find the container

    # enumerate the container with the items that are in it
    quantities = {}
    for skillbook in skillbooks:
        quantities[skillbook["item_type_id"]] = skillbook["quantity"]
    
    #get list of id/items matchings from DB text dump (generated by skillbooks_id_export.py)
    items, itemsbyid = get_item_ids_from_db_dump()

    #get items we're interested in from file
    booknames = [s.strip() for s in open(booklist)]

    bookquantities = []
    for name in booknames:
        quant = {}
        quant["name"] = name
        if not name in items:
            quant["class"] = 'text-warning'
            quant["quantity"] = 'ERROR'
        elif items[name] in quantities:
            quant["quantity"] = quantities[items[name]]
            if quantities[items[name]] < 10:
                quant["class"] = 'text-danger'
            else:
                quant["class"] = 'text-info'
        else:
            quant["quantity"] = 0
            quant["class"] = 'text-danger'
        bookquantities.append(quant)

    if(allitems):
        for skillbook in skillbooks:
            if not itemsbyid[skillbook["item_type_id"]] in booknames:
                quant = {}
                quant["name"] = itemsbyid[skillbook["item_type_id"]]
                quant["class"] = 'text-warning'
                quant["quantity"] = quantities[skillbook["item_type_id"]]
                bookquantities.append(quant)

    return bookquantities

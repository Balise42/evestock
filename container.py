import logging

import evelink

from common import (
    cache,
    corp,
    idmap,
)


def parse_assets(location, assets):
    ctr = Container()
    for i in assets:
        loc_flag = i['location_flag']
        if loc_flag == idmap.invflag["Hangar"]:
            ctr.add_hangars(i)
        elif loc_flag == idmap.invflag["CorpMarket"]:
            ctr.add_deliveries(i)
    cache.save()
    return ctr


class Container:
    def __init__(self, prefix=None):
        self.prefix = prefix
        self.contents = {}
        self.container = {}

    def add_hangars(self, assets):
        hangars = Container(prefix="/hangar/")
        for i in assets['contents']:
            loc_flag = i['location_flag']
            hangar_name = idmap.hangar[loc_flag]
            prefix = "%s/" % hangar_name
            hangar = hangars.container.setdefault(
                hangar_name, Container(prefix))
            hangar.add(i)
        self.container['hangar'] = hangars

    def add_deliveries(self, asset):
        ctr = self.container.setdefault(
            "deliveries", Container("/deliveries/"))
        ctr.add(asset)

    def add(self, entry):
        type_ = idmap.item[entry['item_type_id']]
        if 'contents' in entry:
            if type_ == 'Plastic Wrap':
                # Ignore courier packages.
                return
            name = self.lookup_name(entry['id'])
            prefix = "%s%s/" % (self.prefix, name)
            ctr = self.container.setdefault(name, Container(prefix))
            for i in entry['contents']:
                ctr.add(i)
        else:
            qty = entry['quantity']
            self.contents.setdefault(type_, 0)
            self.contents[type_] += qty

    def lookup_name(self, id_):
        try:
            result = cache.lookup(
                lambda: corp.locations(id_).result,
                "locations", id_, 3600)
            name = result[id_]['name']
        except evelink.api.APIError:
            name = "Unknown"
        return name

    def print_(self):
        for i in sorted(self.contents.keys()):
            logging.debug("%s%s (%d)",
                          self.prefix, i,
                          self.contents[i])
        for i in sorted(self.container.keys()):
            self.container[i].print_()

    def lookup(self, where, type_):
        if len(where) == 0:
            return self.contents.get(type_, 0)
        else:
            try:
                return self.container[where[0]].lookup(where[1:], type_)
            except KeyError:
                return None

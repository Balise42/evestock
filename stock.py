from common import corp, cache, idmap
from config import (
    loc_aliases,
    stations,
)
from report import Report
from station import Station


class Stock(object):
    def __init__(self):
        self.station = {}
        self._stocks = {}
        self.assets = self._get_assets()

        for stn_id, stn_data in stations.iteritems():
            stn_name = idmap.stn[stn_id]
            self.station[stn_name] = Station(stn_id, self.assets)
            self._check_stocks(stn_name, stn_data)

    def _get_assets(self):
        return cache.lookup(
            lambda: corp.assets().result,
            "corpAssets", "corpAssets", 3600)

    def _check_stocks(self, stn_name, stn_data):
        stn_stocks = {}
        for loc_alias, stock_list in stn_data.iteritems():
            where = loc_aliases[loc_alias]
            loc_encoded = "/".join(where)
            stn_stocks.setdefault(loc_encoded, [])
            for type_, target in stock_list:
                have = self.station[stn_name].lookup(where, type_)
                stn_stocks[loc_encoded].append([type_, target, have])
        self._stocks[stn_name] = stn_stocks

    def build_report(self):
        return Report(self._stocks)

import evelink

import common
from config import itemids, stationids, invflags


class Mapper(object):
    def __init__(self, path):
        self._fwd = {}
        self._rev = {}
        self.path = path
        self.load()

    def load(self):
        self._load_from_file()

    def _load_from_file(self):
        with open(self.path, "r") as f:
            for line in f:
                id_, name = line.strip().split(" ", 1)
                id_ = int(id_)
                self._fwd[id_] = name
                self._rev[name] = id_

    def __getitem__(self, query):
        if isinstance(query, int):
            stn, office = IDMap.stn_office_ids(query)
            return self._fwd[stn]
        else:
            return self._rev[query]


class StationIDs(Mapper):
    def load(self):
        super(StationIDs, self).load()
        self._load_from_api()

    def _load_from_api(self):
        eve = evelink.eve.EVE()
        results = common.cache.lookup(
            lambda: eve.conquerable_stations().result,
            "conqStations", "conqStations", 3600, cat_prefix=False)
        for id_, value in results.iteritems():
            name = value['name']
            self._fwd[id_] = name
            self._rev[name] = id_


class HangarIDs(Mapper):
    HANGAR_FLAGNAMES = ["Hangar", "CorpSAG2", "CorpSAG3", "CorpSAG4",
                        "CorpSAG5", "CorpSAG6", "CorpSAG7"]

    def __init__(self, sheet, invflag):
        self.sheet = sheet
        self.invflag = invflag
        super(HangarIDs, self).__init__("")

    def load(self):
        for flag, id_ in zip(self.HANGAR_FLAGNAMES,
                             sorted(self.sheet['hangars'])):
            flagid = self.invflag[flag]
            hangar = self.sheet['hangars'][id_]
            self._fwd[flagid] = hangar
            self._rev[hangar] = flagid


class IDMap(object):
    def __init__(self, corp):
        self.stn = StationIDs(stationids)
        self.item = Mapper(itemids)
        self.invflag = Mapper(invflags)
        self.hangar = HangarIDs(corp, self.invflag)

    @staticmethod
    def stn_office_ids(loc_id):
        stn = office = None

        if(loc_id >= 66000000):
            # It's an office, convert to stationID
            office = loc_id
            if office <= 66014929:
                # Normal/conquerable *station*
                office -= 1
            stn = office - 6000000
        else:
            stn = loc_id
            office = stn + 6000000
            if office < 66014929:
                office += 1
        return stn, office

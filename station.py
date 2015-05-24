from common import idmap
from container import parse_assets


class Station:
    def __init__(self, id_, assets):
        self.stn_id, self.office_id = idmap.stn_office_ids(id_)
        self.name = idmap.stn[id_]
        self.divisions = self.get_local_assets(assets)

    def get_local_assets(self, assets):
        local_assets = []
        if self.stn_id in assets:
            local_assets.extend(assets[self.stn_id]['contents'])
        if self.office_id in assets:
            local_assets.extend(assets[self.office_id]['contents'])
        return parse_assets(self.stn_id, local_assets)

    def lookup(self, where, type_):
        return self.divisions.lookup(where, type_)

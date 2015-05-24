class ReportStn(object):
    def __init__(self, name, stn_data):
        self.name = name
        self._loc = {}
        for loc, loc_data in stn_data.iteritems():
            self._loc[loc] = ReportLoc(loc, loc_data)

    def locs(self):
        for loc in sorted(self._loc):
            yield self._loc[loc]


class ReportLoc(object):
    def __init__(self, name, loc_data):
        self.name = name
        self._item = []
        for item_data in loc_data:
            self._item.append(ReportItem(item_data))

    def items(self):
        for item in self._item:
            yield item


class ReportItem(object):
    def __init__(self, item_data):
        self.name, self.target, self.have = item_data
        if self.have and self.target > 0:
            self.percent = (self.have*100.0)/self.target


class Report(object):
    def __init__(self, stocks):
        self._stn = {}
        for stn, stn_data in stocks.iteritems():
            self._stn[stn] = ReportStn(stn, stn_data)

    def stns(self):
        for stn in sorted(self._stn):
            yield self._stn[stn]

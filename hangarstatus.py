class HangarStatus:
    def __init__(self, stationname, containername, itemlist):
        self.station = Station(stationname)
        self.container = Container(containername, station)
        self.itemlist = itemlist

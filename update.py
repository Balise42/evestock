import webapp2
from google.appengine.api import memcache

from update_ids import get_container_id, get_station_id


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stationid = get_station_id()
        memcache.set("stationid", stationid)
        containerid = get_container_id()
        memcache.set("containerid", containerid)

app = webapp2.WSGIApplication([
    ('/update', MainHandler)
], debug=True)

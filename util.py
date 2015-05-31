import os
import os.path
import logging
import time

try:
    from google.appengine.api import memcache
    CACHETYPE = "memcache"
except ImportError:
    import pickle
    CACHETYPE = "pickle"

import common
from config import log_level


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level))


def setup_cache():
    if CACHETYPE == "pickle":
        return PickleCache()
    elif CACHETYPE == "memcache":
        return MemCache()

class Cache(object):
    def lookup(self, func, category, id_, ttl, cat_prefix=True):
        if cat_prefix:
            category = "%d.%s" % (common.sheet['id'], category)
        return self._lookup(func, category, id_, ttl)

    def save(self):
        pass

class PickleCache(Cache):
    def __init__(self):
        self.filename = "cache/cache.p"
        self.data = self._load()

    def _load(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        else:
            return {}

    def save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)

    def _lookup(self, func, category, id_, ttl):
        self.data.setdefault(category, {})
        if id_ in self.data[category]:
            timestamp, value = self.data[category][id_]
            delta = time.time() - timestamp
            if delta <= ttl:
                logging.debug("PickleCache:%s:%s - Fresh cache entry",
                              category, id_)
                return value
            else:
                logging.debug("PickleCache:%s:%s - Stale cache entry, updating",
                              category, id_)
        else:
            logging.debug("PickleCache:%s:%s - No cache entry, updating",
                          category, id_)
        return self._update(func, category, id_)

    def _update(self, func, category, id_):
        value = func()
        now = time.time()
        self.data[category][id_] = [now, value]
        return value


class MemCache(Cache):
    def _lookup(self, func, category, id_, ttl):
        id_ = str(id_)
        data = memcache.get(id_, namespace=category)
        if data is None:
            logging.debug("MemCache:%s:%s - No cache entry, updating",
                          category, id_)
            data = func()
            memcache.add(id_, data, namespace=category, time=ttl)
        else:
            logging.debug("MemCache:%s:%s - Fresh cache entry", category, id_)
        return data

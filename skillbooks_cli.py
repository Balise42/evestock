#!/usr/bin/python
import evelink
import sqlite3
import pprint

from keys import keyid, vcode
from config import stationid, smallcontainerid, dbname, booklist
from skillbooks_stock import get_quantities

quantities = get_quantities()

for name, quantity in quantities.iteritems():
    print name, quantity["quantity"]

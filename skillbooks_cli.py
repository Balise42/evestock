#!/usr/bin/python
import evelink
import sqlite3
import pprint

from keys import keyid, vcode
from skillbooks_stock import get_quantities

quantities = get_quantities()

for quantity in quantities:
    print quantity["name"], quantity["quantity"]

#!/usr/bin/python
import sqlite3

from skillbooks_stock import get_quantities

quantities = get_quantities()

for quantity in quantities:
    print quantity["name"], quantity["quantity"]

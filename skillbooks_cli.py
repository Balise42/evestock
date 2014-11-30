#!/usr/bin/python
import sqlite3

from stock import Stock

stock = Stock()

for quantity in stock.list_of_items:
    print quantity["name"], quantity["quantity"]

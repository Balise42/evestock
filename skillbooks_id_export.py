#!/usr/bin/python

import sqlite3
from config import dbname, bookids

conn = sqlite3.connect(dbname)
conn.text_factory = str
c = conn.cursor()
items = {}
c.execute("SELECT typeId, typeName from invTypes")
f = open(bookids, 'w')
for(itemid, name) in c:
        f.write(itemid.__str__())
        f.write(' ')
        f.write(name)
        f.write('\n')


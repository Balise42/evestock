#!/usr/bin/python

import sqlite3
from config import dbname, itemids, stationids, invflags

query_map = [
    [stationids, "SELECT stationID, stationName from staStations"],
    [itemids, "SELECT typeId, typeName from invTypes"],
    [invflags, "SELECT flagID, flagName from invFlags"],
]


def export(cursor, path, query):
    cursor.execute(query)
    with open(path, 'w') as output:
        for(id_, name) in cursor:
            output.write("%s %s\n" % (id_, name))


def main():
    conn = sqlite3.connect(dbname)
    conn.text_factory = str
    cursor = conn.cursor()
    for path, query in query_map:
        export(cursor, path, query)
    conn.close()

if __name__ == '__main__':
    main()

#!/usr/bin/python

import sqlite3
from config import dbname, bookids

class IdExport:
  def __init__(self):
    self.file_to_write = open(bookids, 'w')
    self.conn = sqlite3.connect(dbname)
    self.conn.text_factory = str
    self.cursor = self.conn.cursor()

  def get_items(self):
    self.cursor.execute("SELECT typeId, typeName from invTypes")

  def run(self):
    self.get_items()
    for(itemid, itemname) in self.cursor:
      self.write_item_to_file(itemid, itemname)

  def write_item_to_file(self, itemid, itemname):
      file_to_write.write(itemid.__str__())
      file_to_write.write(' ')
      file_to_write.write(itemname)
      file_to_write.write('\n')

if __name__ == '__main__':
  IdExport().run()

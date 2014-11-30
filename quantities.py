class Quantities:
  def __init__(self):
    self.quantities = {}

  def add(self, itemid, quantity):
    if(itemid in self.quantities):
      self.quantities[itemid] = self.quantities[itemid] + quantity
    else:
      self.quantities[itemid] = quantity

  def get_quantity(self, itemid):
    return self.quantities[itemid]

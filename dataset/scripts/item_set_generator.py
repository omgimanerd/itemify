#!/usr/bin/python
# This class handles the generation of the item set JSON following the
# standards used by League of Legends, found here:
# https://developer.riotgames.com/docs/item-sets

from util import Util

class ItemSetBlockItems():
  def __init__(self):
    self.items = []

  def getItems(self):
    return self.items

  def addItem(self, id, count):
    self.items.append({
        'id': str(id),
        'count': count
    })


class ItemSetGenerator():
  def __init__(self, json):
    self.json = json

  @staticmethod
  def create(title):
    json = {
      'title': title,
      'type': 'custom',
      'map': 'any',
      'mode': 'any',
      'priority': True,
      'blocks': []
    }
    return ItemSetGenerator(json)

  def getItemSet(self):
    return self.json

  def addBlock(self, name, recMath, items):
    block = {
      'type': name,
      'recMath': recMath,
      'items': items
    }
    self.json['blocks'].append(block)

"""
This main() method is for testing purposes only.
"""
def main():
  generator = ItemSetGenerator.create("test")
  items = ItemSetBlockItems()
  items.addItem(1001, 1)
  items.addItem(3139, 1)
  items.addItem(3141, 1)
  generator.addBlock('test', True, items.getItems())
  print Util.json_dump(generator.getItemSet())

if __name__ == '__main__':
  main()

#!/usr/bin/python
# This class handles the generation of the item set JSON following the
# standards used by League of Legends, found here:
# https://developer.riotgames.com/docs/item-sets

from util import Util

class ItemSetBlockItems():
  def __init__(self):
    self.items = []

  def get_items(self):
    return self.items

  def add_item(self, id, count):
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

  def get_item_set(self):
    return self.json

  def add_block(self, name, recMath, items):
    block = {
      'type': name,
      'recMath': recMath,
      'items': items
    }
    self.json['blocks'].append(block)

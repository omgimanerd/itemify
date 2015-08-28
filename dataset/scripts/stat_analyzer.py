#!/usr/bin/python
# This class helps with the statistical analysis of the aggregated data and
# allows the data to be matched to champions and items. Unicode to bytestring
# conversion is taken care of in this class.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json

class StatAnalyzer():
  def __init__(self, champions, items, stats):
    self.champions = champions
    self.items = items
    self.stats = stats

  @staticmethod
  def create():
    with open('../champions.json') as champions_input:
      champions = json.loads(champions_input.read())
    with open('../items.json') as items_input:
      items = json.loads(items_input.read())
    with open('../stats.json') as stats_input:
      stats = map(json.loads, stats_input.readlines())
    print "Read stats, total entries %s" % len(stats)
    return StatAnalyzer(champions, items, stats)

  def get_champion_name_by_id(self, id):
    for champion in self.champions:
      if self.champions[champion]['id'] == id:
        return champion
    return None

  def get_champion_data_by_name(self, champion):
    return self.champions.get(str(champion), None)

  def get_champion_data_by_id(self, id):
    return self.get_champion_data_by_name(self.get_champion_name_by_id(id))

  def get_item_name_by_id(self, id):
    item = self.items.get(str(id), None)
    if item:
      return str(item['name'])
    return None

  def get_item_id_by_name(self, itemName):
    for item in self.items:
      if str(self.items[item]['name']) == str(itemName):
        return int(item)
    return None

  def get_item_data_by_id(self, id):
    return self.items.get(str(id), None)

  def get_item_data_by_name(self, item):
    return self.get_item_data_by_id(self.get_item_id_by_name(item))

"""
This main() method is for testing purposes only.
"""
def main():
  analyzer = StatAnalyzer.create()
  print analyzer.get_champion_name_by_id(266)
  print analyzer.get_champion_data_by_name('Annie')
  print analyzer.get_champion_data_by_id(266)
  print analyzer.get_item_name_by_id(1001)
  print analyzer.get_item_id_by_name('Boots of Speed')
  print analyzer.get_item_data_by_id(1001)
  print analyzer.get_item_data_by_name('Pickaxe')

if __name__ == '__main__':
  main()

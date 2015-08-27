#!/usr/bin/python

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
      stats = map(json.loads, stats_input.read().split('\n')[:-1])
    print "Read stats, total entries %s" % len(stats)
    return StatAnalyzer(champions, items, stats)

  def getChampionNameById(self, id):
    for champion in self.champions:
      if self.champions[champion]['id'] == id:
        return champion
    return None

  def getItemNameById(self, id):
    for item in self.items:
      if self.items[item]['id'] == id:
        return self.items[item]['name']
    return None

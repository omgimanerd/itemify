#!/usr/bin/python

import json

class StatAnalyzer():
  def __init__(self):
    with open('../champions.json') as champions_input:
      self.champions = json.loads(champions_input.read())
    with open('../items.json') as items_input:
      self.items = json.loads(items_input.read())
    with open('../stats.json') as stats_input:
      self.stats = stats_input.read().split('\n')[:-1]
    print "Read stats, total entries %s" % len(stats)

  def getChampionNameById(self, id):
    for champion in champions:
      if champion['id'] == id:
        return champion
    return None

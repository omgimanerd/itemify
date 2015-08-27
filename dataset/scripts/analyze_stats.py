#!/usr/bin/python

import json

from stat_analyzer import StatAnalyzer

def main():
  analyzer = StatAnalyzer.create()

  with open('../stats.json') as stats_input:
    stats = map(json.loads, stats_input.read().split("\n")[:-1])

  # by_champion is a object with 126 keys, one for each champion id.
  # The value assigned to each key is a list of their game data generated
  # from stats.json
  by_champion = {}
  for stat in stats:
    champion = stat['champion']
    if by_champion.get(champion, None):
      by_champion[champion].append(stat)
    else:
      by_champion[champion] = [stat]

  # build_stats is an object with 126 keys, one for each champion id.
  # The value assigned to each key is a dict of the format:
  # { itemId: frequency, itemId: frequency ...... }
  build_stats = {}
  for champion in by_champion:
    championName = str(analyzer.getChampionNameById(champion))
    build_stats[championName] = {}
    for game in by_champion[champion]:
      for i in range(1, 7):
        item = str(analyzer.getItemNameById(game.get('item%s' % i, None)))
        if build_stats[championName].get(item, None):
          build_stats[championName][item] += 1
        else:
          build_stats[championName][item] = 1
  
  for champion in build_stats:
    print '%s: %s' % (champion, build_stats[champion])

if __name__ == '__main__':
  main()
      

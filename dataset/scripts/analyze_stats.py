#!/usr/bin/python

import json

from stat_analyzer import StatAnalyzer

def main():
  analyzer = StatAnalyzer.create()

  with open('../stats.json') as stats_input:
    stats = stats_input.read().split("\n")[:-1]
  
  print "Read stats, total entries %s" % len(stats)

  print analyzer.getItemNameById(3911)
  print analyzer.getItemNameById(3710)

  by_champion = {}
  for stat in stats:
    stat = json.loads(stat)
    champion = stat['champion']
    if by_champion.get(champion, None):
      by_champion[champion].append(stat)
    else:
      by_champion[champion] = [stat]


if __name__ == '__main__':
  main()
      

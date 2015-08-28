#!/usr/bin/python
# This is the main script that takes care of generating the champion build file.
# It uses the StatAnalyzer class to parse through the main dataset of about
# ~150000 games and generates an optimal build for every champion.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

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
  # { itemId: effectivenessScore, itemId: effectivenessScore ...... }
  # effectivenessScore is a score of the item's effectiveness based on
  # win and KDA, and increases linearly with number of times built.
  build_stats = {}
  for champion in by_champion:
    championName = analyzer.get_champion_name_by_id(champion)
    build_stats[championName] = {}
    for game in by_champion[champion]:
      kda = 0
      if game['kills']:
        kda += game['kills']
      if game['assists']:
        kda += game['assists'] / 2
      if game['deaths']:
        kda /= float(game['deaths'])
      kda -= 1
      effectivenessScore = kda
      if game.get('win', False):
        effectivenessScore += 2
      for i in range(1, 7):
        item = str(analyzer.get_item_name_by_id(game.get('item%s' % i, None)))
        if not item == 'None':
          if build_stats[championName].get(item, None):
            build_stats[championName][item] += effectivenessScore
          else:
            build_stats[championName][item] = effectivenessScore

  for champion in build_stats:
    with open('../stats-by-champion/%s.json' % champion, 'w') as champion_output:
      champion_output.write(json.dumps(
        sorted(build_stats[champion], key=build_stats[champion].get)[::-1]))
    print '%s: %s' % (champion, sorted(build_stats[champion],
                                       key=build_stats[champion].get)[::-1])

if __name__ == '__main__':
  main()


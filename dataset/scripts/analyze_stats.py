#!/usr/bin/python
# This is the main script that takes care of generating the champion build file.
# It uses the StatAnalyzer class to parse through the main dataset of about
# ~150000 games and generates an optimal build for every champion.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json

from util import Util
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
        item = game.get('item%s' % i, None)
        if item:
          if build_stats[championName].get(item, None):
            build_stats[championName][item] += effectivenessScore
          else:
            build_stats[championName][item] = effectivenessScore

  # The build stats will be written into the /stats-by-champion directory
  # with one JSON file per champion. We split this build data into viable
  # end game builds and intermediate builds by sorting the build data by
  # effectiveness score and parsing it then.
  for champion in build_stats:
    build = sorted(build_stats[champion], key=build_stats[champion].get)[::-1]
    build_output = {
      'trinkets': [],
      'boots': [],
      'endgame': [],
      'consumables': []
    }
    for item in build:
      if analyzer.is_irrelevant(item):
        continue
      elif analyzer.is_trinket(item):
        build_output['trinkets'].append(item)
      elif analyzer.is_boot(item):
        build_output['boots'].append(item)
      elif analyzer.is_consumable(item):
        build_output['consumables'].append(item)
      elif not analyzer.get_items_built_from(item):
        build_output['endgame'].append(item)

    for category in build_output:
      build_output[category] = map(analyzer.get_item_name_by_id,
                                   build_output[category])

    with open('../stats-by-champion/%s.json' % champion,
              'w') as champion_output:
      champion_output.write(Util.json_dump(build_output))
    print 'Sucessfully wrote %s.json' % champion

if __name__ == '__main__':
  main()


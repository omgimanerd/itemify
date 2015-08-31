#!/usr/bin/python
# This is the main script that takes care of generating the champion build file.
# It uses the StatAnalyzer class to parse through the main dataset of about
# ~150000 games and generates an optimal build for every champion.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

from operator import itemgetter
import json

from item_set_generator import ItemSetBlockItems
from item_set_generator import ItemSetGenerator
from util import Util
from stat_analyzer import StatAnalyzer

# For each category of items, we will impose a limit on the max number of
# items we show, we will also specify here whether or not we will sort the
# category by item tier.
CATEGORIES = [
  'Trinkets', 'Consumables', 'Boots', 'Jungle', 'Endgame', 'Elixirs'
]
ITEM_LIMIT = {
  'Trinkets': 4,
  'Boots': 3,
  'Jungle': 3,
  'Elixirs': 2,
  'Consumables': 10,
  'Endgame': 7
}
SORT_TIER = {
  'Trinkets': True,
  'Boots': True,
  'Jungle': True,
  'Elixirs': False,
  'Consumables': False,
  'Endgame': False
}

def main():
  analyzer = StatAnalyzer.create()

  with open('../stats.json') as stats_input:
    stats = map(json.loads, stats_input.readlines())

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
    # trinkets, boots, endgame, and consumables all store items that people
    # have built for this champion, sorted in order of effectiveness.
    # buildObj is a dict that when dumped to a JSON object, becomes a valid
    # build file that someone can put in the League of Legends directory and
    # use.
    build_output = {}
    for category in CATEGORIES:
      build_output[category] = []

    effectiveness_sorted_items = sorted(build_stats[champion],
                                        key=build_stats[champion].get)[::-1]
    for item in effectiveness_sorted_items:
      if analyzer.is_irrelevant(item) or not analyzer.get_item_name_by_id(item):
        continue
      elif analyzer.is_trinket(item):
        build_output['Trinkets'].append(item)
      elif analyzer.is_boot(item):
        build_output['Boots'].append(item)
      elif analyzer.is_jungle(item):
        build_output['Jungle'].append(item)
      elif analyzer.is_elixir(item):
        build_output['Elixirs'].append(item)
      elif analyzer.is_consumable(item):
        build_output['Consumables'].append(item)
      elif not analyzer.get_items_built_from(item):
        build_output['Endgame'].append(item)

    # For each category of item, we will only show a certain number of items and
    # will will generate the item set for each category. We will also sort
    # the items on build tree, where lower tier items will come first.
    generator = ItemSetGenerator.create(champion)
    for category in CATEGORIES:
      build_output[category] = build_output[category][:ITEM_LIMIT[category]]
      if SORT_TIER[category]:
        build_output[category] = sorted(
            build_output[category],
            key=lambda item: analyzer.get_item_data_by_id(item).get('depth', 0))

      items = ItemSetBlockItems()
      for item in build_output[category]:
        items.add_item(item, 1)
      generator.add_block('Recommended %s' % category, False, items.get_items())

      build_output[category] = map(
          analyzer.get_item_name_by_id, build_output[category])

    item_set = generator.get_item_set()

    # We will write the build JSON file to one file and the parsed data to
    # another.
    data_file = Util.normalize_champion_name(champion)
    with open('../builds/%s.json' % data_file,
              'w') as champion_output:
      champion_output.write(Util.json_dump(build_output))
      print 'Wrote %s.json' % data_file

    # As of now, only the build files are used, but we will store the champion
    # data as well for future extendability.
    build_file = '%s_build' % Util.normalize_champion_name(champion)
    with open('../builds/%s.json' % build_file,
              'w') as build_file_output:
      build_file_output.write(Util.json_dump(item_set))
      print 'Wrote %s.json' % build_file

  print 'Successfully wrote champion data.'

if __name__ == '__main__':
  main()

#!/usr/bin/python

import json

from data_aggregator import DataAggregator

SEEDING_SUMMONERS = ['WildTurtle', 'Bjergsen']

def main():
  data = DataAggregator.create()

  seed_ids = data.get_summoner_ids(SEEDING_SUMMONERS)
  stats, result_ids = data.get_build_data(seed_ids)

  with open('../stats.json', 'a') as stats_output:
    for stat in stats:
      stats_output.write('%s\n' % json.dumps(stat))

  with open('../queried_summoners', 'w') as queried_summoners_output:
    for id in seed_ids:
      queried_summoners_output.write('%s\n' % id)
  
  with open('../unqueried_summoners', 'w') as unqueried_summoners_output:
    for id in result_ids:
      unqueried_summoners_output.write('%s\n' % id)

if __name__ == '__main__':
  main()

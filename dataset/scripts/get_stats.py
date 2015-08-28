#!/usr/bin/python
# This script is run after get_stats_from_seed under the assumption that
# queried_summoners, unqueried_summoners, and stats.json have been
# initialized by it. It will query all the unqueried summoners and continue
# adding to the list of unqueried summoners while updating the list of
# queried summoners.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json
import time

from data_aggregator import DataAggregator

QUERY_DELAY = 2;

def main():
  data = DataAggregator.create()

  with open('../queried_summoners', 'r') as queried_summoners_input:
    queried_summoners = queried_summoners_input.readlines()

  with open('../unqueried_summoners', 'r') as unqueried_summoners_input:
    unqueried_summoners = unqueried_summoners_input.readlines()

  print 'Queried: %s' % ', '.join(queried_summoners)
  print 'Unqueried: %s' % ', '.join(unqueried_summoners)

  new_aggregated_summoners = []

  for id in unqueried_summoners:
    if id in queried_summoners:
      print 'ID %s has already been queried' % id
      continue

    stats, aggregated_summoners = data.get_build_data([id])

    with open('../stats.json', 'a') as stats_output:
      for stat in stats:
        stats_output.write('%s\n' % json.dumps(stat))

    with open('../queried_summoners', 'a') as queried_summoners_output:
      queried_summoners_output.write('%s\n' % id)
    queried_summoners.append(id)

    new_aggregated_summoners += aggregated_summoners

    time.sleep(QUERY_DELAY)

  new_unqueried_summoners = []
  for summoner in new_aggregated_summoners:
    if summoner not in queried_summoners:
      new_unqueried_summoners.append(summoner)

  with open('../unqueried_summoners', 'w') as unqueried_summoners_output:
    for id in new_unqueried_summoners:
      unqueried_summoners_output.write('%s\n' % id)

if __name__ == '__main__':
  main()

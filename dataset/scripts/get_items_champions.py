#!/usr/bin/python
# This script uses the DataAggregator class to pull static data from Riot's API,
# namely the list of all the items and champions.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

from util import Util
from data_aggregator import DataAggregator

def main():
  data = DataAggregator.create()

  with open('../items.json', 'w') as items_output:
    items_output.write(Util.json_dump(data.get_items()))
  print 'Successfully wrote items.json'

  with open('../champions.json', 'w') as champions_output:
    champions_output.write(Util.json_dump(data.get_champions()))
  print 'Successfully wrote champions.json'

if __name__ == '__main__':
  main()

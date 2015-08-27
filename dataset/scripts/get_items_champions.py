#!/usr/bin/python

import json

from riot_api import RiotApi

def main():
  data = DataAggregator()

  with open('../items.json', 'w') as items_output:
    items_output.write(data.parse_json(data.get_items()))
  print 'Successfully wrote items.json'

  with open('../champions.json', 'w') as champions_output:
    champions_output.write(data.parse_json(data.get_champions()))
  print 'Successfully wrote champions.json'

if __name__ == '__main__':
  main()

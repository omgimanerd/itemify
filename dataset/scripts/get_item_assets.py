#!/usr/bin/python
# This script downloads all the League of Legends item image assets
# from DataDragon into our static assets folder. There isn't always an image
# asset for every item ID, so this will hit 404 for a majority of the links.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json
import os
import time

WGET_COMMAND = ('wget http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/%s.png'
                ' -O ../../static/images/items/%s.png')

def main():
  with open('../items.json') as items_input:
    items = json.loads(items_input.read())

  for item in items.keys():
    os.system(WGET_COMMAND % (item, item))

if __name__ == '__main__':
  main()

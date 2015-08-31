#!/usr/bin/python
# This script takes all the images in /dataset/build_images and crops the item
# build out of them and renames them to the champion to which they correspond
# to.
# This script should only be run under the assumption that the images in the
# direction were freshly loaded from the League of Legends Screenshot directory,
# with one image for each champion build prenamed in numerical order corresponding
# to the champions' alphabetical order.
# This script must be run inside the build_images folder since it uses the os
# module which works using the current terminal context.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json
from PIL import Image
import os

def main():
  with open('../champions.json') as champions_input:
    champions = json.loads(champions_input.read())
  champion_names = sorted(champions, key=lambda x: champions[x]['name'])

  i = 1
  for name in champion_names:
    print 'mv Screen{:02d} {}_build.png'.format(i, name.lower())
    os.system('mv Screen{:02d}.png {}_build.png'.format(i, name.lower()))
    i += 1


if __name__ == '__main__':
  main()

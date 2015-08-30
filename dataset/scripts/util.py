#!/usr/bin/python
# This file contains utility methods encapsulated by a Util class.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json
import re

class Util():

  @staticmethod
  def json_dump(obj):
    return json.dumps(obj, sort_keys=True, encoding='utf-8',
                      indent=2, separators=(',', ': '))

  @staticmethod
  def normalize_champion_name(name):
    return re.sub('[^a-zA-Z]', '', name).lower()

"""
This main() method is for testing purposes only.
"""
def main():
  print Util.normalize_champion_name("Kha'Zix")

if __name__ == '__main__':
  main()

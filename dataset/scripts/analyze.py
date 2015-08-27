#!/usr/bin/python

import json

def main():
  by_champion = {}
  for stat in stats:
    stat = json.loads(stat)
    champion = stat['champion']
    if by_champion.get(champion, None):
      by_champion[champion].append(stat)
    else:
      by_champion[champion] = [stat]
    print "\n\n\n"
    print by_champion

if __name__ == '__main__':
  main()

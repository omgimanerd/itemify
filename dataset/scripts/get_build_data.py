#!/usr/bin/python

import json

from riot_api import RiotApi

SEEDING_SUMMONERS = ['WildTurtle', 'Bjergsen']

def main():
  api = RiotApi()
  API_KEY = api.get_api_key()

  api = RiotApi()

  summoners_request_path = '/api/lol/na/v1.4/summoner/by-name/%s' % (
    ','.join(SEEDING_SUMMONERS))
  summoners_request_params = {
    'api_key': API_KEY
  }
  summoners = api.get(summoners_request_path,
                      summoners_request_params)
  ids = []
  for summoner in summoners:
    ids.append(summoners[summoner]['id'])

  games_request_path = '/api/lol/na/v1.3/game/by-summoner/%s/recent'
  games_request_params = {
    'api_key': API_KEY
  }

  data = []
  aggregatedIds = []
  for id in ids:
    print id
    games = api.get(games_request_path % id, games_request_params)['games']
    for game in games:
      itemStat = {
        'champion': game['championId'],
        'item1': game['stats']['item1'],
        'item2': game['stats']['item2'],
        'item3': game['stats']['item3'],
        'item4': game['stats']['item4'],
        'item5': game['stats']['item5'],
        'item6': game['stats']['item6']
      }
      data.append(itemStat)
      aggregatedIds.append('')

if __name__ == '__main__':
  main()

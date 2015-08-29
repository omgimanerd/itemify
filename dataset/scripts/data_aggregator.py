#!/usr/bin/python
# This class takes care of aggregating data from the Riot API and has methods
# that convert the aggregated data into a form that we can parse, store, and
# display.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json

from riot_api import RiotApi

class DataAggregator():
  def __init__(self, api_key):
    self.api_key = api_key

  @staticmethod
  def create():
    api_key = RiotApi.get_default_api_key()
    return DataAggregator(api_key)

  def parse_json(self, obj):
    return json.dumps(obj, sort_keys=True, encoding='utf-8',
                      indent=2, separators=(',', ': '))

  def get_items(self):
    items_request_path = '/api/lol/static-data/na/v1.2/item'
    items_request_params = {
      'locale': 'en_US',
      'itemListData': 'all',
      'api_key': self.api_key
    }
    return RiotApi.get(items_request_path,
                       items_request_params).get('data', None)

  def get_champions(self):
    champions_request_path = '/api/lol/static-data/na/v1.2/champion'
    champions_request_params = {
      'locale': 'en_US',
      'champData': 'tags',
      'api_key': self.api_key
    }
    return RiotApi.get(champions_request_path,
                       champions_request_params).get('data', None)

  def get_summoner_ids(self, summoner_names):
    summoners_request_path = '/api/lol/na/v1.4/summoner/by-name/%s' % (
      ','.join(summoner_names))
    summoners_request_params = {
      'api_key': self.api_key
    }
    summoners = RiotApi.get(summoners_request_path, summoners_request_params)
    ids = []
    for summoner in summoners:
      ids.append(summoners[summoner].get('id', None))
    return ids

  def get_build_data(self, ids):
    data = []
    aggregatedIds = []

    games_request_path = '/api/lol/na/v1.3/game/by-summoner/%s/recent'
    games_request_params = {
      'api_key': self.api_key
    }

    for id in ids:
      print 'Querying summoner id: %s' % id
      games = RiotApi.get(games_request_path % id,
                          games_request_params)['games']
      for game in games:
        output = {}
        output['champion'] = game.get('championId', None)
        stats = game.get('stats', None)
        if stats:
          output['item1'] = stats.get('item1', None)
          output['item2'] = stats.get('item2', None)
          output['item3'] = stats.get('item3', None)
          output['item4'] = stats.get('item4', None)
          output['item5'] = stats.get('item5', None)
          output['item6'] = stats.get('item6', None)
          output['win'] = stats.get('win', None)
          output['kills'] = stats.get('championsKilled', None)
          output['deaths'] = stats.get('numDeaths', None)
          output['assists'] = stats.get('assists', None)
        data.append(output)

      fellowPlayers = game.get('fellowPlayers', None)
      if fellowPlayers:
        for fellowPlayer in fellowPlayers:
          aggregatedIds.append(fellowPlayer.get('summonerId', None))
    return data, list(set(aggregatedIds))

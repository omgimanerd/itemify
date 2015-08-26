#!/usr/bin/python

import json

from riot_api import RiotApi

def main():
  api = RiotApi()
  API_KEY = api.get_api_key()

  with open('../items.json', 'w') as items_output:
    items_request_path = '/api/lol/static-data/na/v1.2/item'
    items_request_params = {
      'locale': 'en_US',
      'itemListData': 'inStore',
      'api_key': API_KEY
    }
    items_raw = api.get(items_request_path, items_request_params)['data']
    items_json = json.dumps(items_raw, sort_keys=True, encoding='utf-8',
                            indent=2, separators=(',', ': '))
    items_output.write(items_json)
  print 'Successfully wrote items.json'

  with open('../champions.json', 'w') as champions_output:
    champions_request_path = '/api/lol/static-data/na/v1.2/champion'
    champions_request_params = {
      'locale': 'en_US',
      'champData': 'tags',
      'api_key': API_KEY
    }
    champions_raw = api.get(champions_request_path,
                            champions_request_params)['data']
    champions_json = json.dumps(champions_raw, sort_keys=True, encoding='utf-8',
                                indent=2, separators=(',', ': '))
    champions_output.write(champions_json)
  print 'Successfully wrote champions.json'

if __name__ == '__main__':
  main()

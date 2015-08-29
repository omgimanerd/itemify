#!/usr/local/bin/python

import json
import requests

API_KEY = None
BASE_URL = 'https://na.api.pvp.net'

def getApiKey():
  f = open('.api_key')
  key = f.read()
  f.close()
  return key

def main():
  # Before all requests to Riot can be made, we must get the API Key.
  API_KEY = getApiKey()
  if not API_KEY:
    raise Error('Put your API Key in a .api_key file!')

  items_request_path = '/api/lol/static-data/na/v1.2/item'
  items_request_params = {
    'locale': 'en_US',
    'itemListData': 'inStore',
    'api_key': API_KEY
  }
  items_request = requests.get("%s%s" % (BASE_URL, items_request_path),
                               params = items_request_params)
  items_raw = json.loads(items_request.text)['data']
  items_json = json.dumps(items_raw, sort_keys=True, encoding='utf-8', indent=2,
                          separators=(',', ': '))
  items_output = open('items.json', 'w')
  items_output.write(items_json)
  items_output.close()
  print 'Successfully wrote items.json'

  champions_request_path = '/api/lol/static-data/na/v1.2/champion'
  champions_request_params = {
    'locale': 'en_US',
    'champData': 'tags',
    'api_key': API_KEY
  }
  champions_request = requests.get("%s%s" % (BASE_URL, champions_request_path),
                                   params = champions_request_params)
  champions_raw = json.loads(items_request.text)['data']
  champions_json = json.dumps(champions_raw, sort_keys=True, encoding='utf-8',
                              indent=2, separators=(',', ': '))
  champions_output = open('champions.json', 'w')
  champions_output.write(champions_json)
  champions_output.close()
  print 'Successfully wrote champions.json'

if __name__ == '__main__':
  main()

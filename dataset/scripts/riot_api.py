#!/usr/bin/python

import json
import requests
import urllib3

urllib3.disable_warnings()

BASE_URL = 'https://na.api.pvp.net'

class RiotApi():

  def get_api_key(self):
    with open('.api_key') as f:
      api_key = f.read()
    if api_key:
      return api_key
    else:
      raise Error('No API key found!')

  def get(self, path, params):
    response = requests.get("%s%s" % (BASE_URL, path), params=params)
    return json.loads(response.text)
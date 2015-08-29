#!/usr/bin/python
# This file contains utility methods encapsulated by a Util class.
# Author: Alvin Lin (alvin.lin@stuypulse.com)

import json

class Util():

  @staticmethod
  def json_dump(obj):
    return json.dumps(obj, sort_keys=True, encoding='utf-8',
                      indent=2, separators=(',', ': '))

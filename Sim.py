#!/usr/bin/env python

import sys
import math
import json
import GBodies

with open('Bodies.json', 'r') as f:
    data = json.load(f)

print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))

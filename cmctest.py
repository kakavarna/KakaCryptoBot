#MODULE IMPORTS
import sys
import json
import util

data = util.getLatest_CMCdata()

for ticker in data:
    print(f"({ticker['symbol']}){ticker['name']}")
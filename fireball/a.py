#https://ssd-api.jpl.nasa.gov/doc/fireball.html

import json
import pandas as pd
import requests
from pandas.io.json import json_normalize

#url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2022-01-01&req-loc=true&limit=2"
#res = requests.get(url)
#var = json.loads(res.text)

#with open("sample.json", "w") as outputFile:
#  json.dump(var, outputFile)

df = pd.read_json("sample.json")

#df = pd.read_json(data)
print(df)

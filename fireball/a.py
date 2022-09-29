#https://ssd-api.jpl.nasa.gov/doc/fireball.html

import json
from numpy import append
import pandas as pd
import requests
from pandas.io.json import json_normalize

#url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2022-01-01&req-loc=true&limit=2"
#res = requests.get(url)
#var = json.loads(res.text)

#with open("sample.json", "w") as outputFile:
#  json.dump(var, outputFile)

with open("sample.json", "r") as f:
  data = json.load(f)

shapedData = {}
for i,fieldName in enumerate(data["fields"]):
  for j,row in enumerate(data["data"]):
    shapedData[fieldName] = row[i]
    


print(shapedData)
#print(data)
#df = pd.DataFrame(data["data"])
#print(df)

import requests as req
import os
import pandas as pd
import json
from datetime import datetime

now_str = datetime.now().strftime("%Y-%m-%d %H%I%S")

try:
    res = req.get('https://mpbais.motcmpb.gov.tw/aismpb/tools/geojsonais.ashx')
except Exception as e:
    print(e)
    # To Do Something

with open(f'./{now_str}-origin-source.json', 'w') as f:
    f.write(res.text)
    f.close()

json_data = json.loads(res.text)

result = {
    "fid": [],
    "IMO_Number": [],
    "Call_Sign": [],
    "ShipName": [],
    "MMSI": [],
    "Navigational_Status": [],
    "SOG": [],
    "Longitude": [],
    "Latitude": [],
    "COG": [],
    "Ship_and_Cargo_Type": [],
    "Record_Time": [],
}

for feature in json_data["features"]:
    if(feature["properties"]["Ship_and_Cargo_Type"] == 80):
        for key, value in feature["properties"].items():
            result[key].append(value)

df = pd.read_json(json.dumps(result))
print(df)

df.to_csv(f'{now_str}-resule.csv', encoding='utf8', index=False)

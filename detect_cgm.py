from email import header
import pandas as pd
import matplotlib.pyplot as plt
import time
import urllib.request as urllib2
import json

# load data from csv
df = pd.read_csv('data/measurements.csv', header=None)

# for i in range(df.shape[0]):
#     # if i != 0:
#     #     continue
#     df1=df.iloc[[i]]
#     print(df1.values[0][0])
#     # print(df.head(5))

while True:
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            print(int(df.values[i][j]))
            data = {"value": int(df.values[i][j])}
            # data = {"value": int(4)}
            req = urllib2.Request("http://localhost:8800/cgmStreamPy")
            # req.add_header("Content-Type", "application/json")
            # urllib2.urlopen(req, data=bytes(data)).read()
            
            urllib2.urlopen(req, data=bytes(json.dumps(data), encoding="utf-8")).read()
            # urllib2.urlopen(req, data=json.dumps(data)).read()

            time.sleep(1.0)
            # print(df.iloc[[i]].values[0][j])

# print(df.values[1][0])
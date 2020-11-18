#|-----------+--------------------+---------------------+-------------------+
# Name:        USDT增发数据/灰度基金持仓数据
# Author:      奥宽量化(www.aoquant.com)
# Created:     2020-11-18
#|-----------+--------------------+---------------------+-------------------+
import requests
import pandas as pd
import json

r = requests.get('https://api.aoquant.com/usdt')
# r = requests.get('https://api.aoquant.com/grayscale')
r= json.loads(r.text)

# print(r)

df = pd.DataFrame(r['result'])
print(df)

# api
AoQuant（奥宽量化）
免费提供数字货币量化开放式API数据接口
奥宽量化官网 https://www.aoquant.com

# 开始：
import requests
import pandas as pd
import json

r = requests.get('https://api.aoquant.com/usdt')
# r = requests.get('https://api.aoquant.com/grayscale')
r= json.loads(r.text)

df = pd.DataFrame(r['result'])
print(df)

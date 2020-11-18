import requests
import pandas as pd
import json

r = requests.get('https://api.aoquant.com/usdt')
# r = requests.get('https://api.aoquant.com/grayscale')
r= json.loads(r.text)

# print(r)

df = pd.DataFrame(r['result'])
print(df)
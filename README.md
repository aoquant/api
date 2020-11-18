# AoQuant_API
> AoQuant（奥宽量化）
免费提供数字货币量化API数据接口
https://www.aoquant.com

# 开始：
```python
import requests
import pandas as pd
import json

#USDT增发数据
r = requests.get('https://api.aoquant.com/usdt')

#灰度基金持仓数据
# r = requests.get('https://api.aoquant.com/grayscale')

r= json.loads(r.text)

df = pd.DataFrame(r['result'])
print(df)
```

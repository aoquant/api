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

#### ##### 返回数据：
USDT增发数据:
{"datetime":"2020-11-18 08:00:37","total_assets":18184204770,"total_liabilities":18024594847}

灰度基金持仓数据:
{"position":513392,"price":17674.5,"timestamp":1605657000000}

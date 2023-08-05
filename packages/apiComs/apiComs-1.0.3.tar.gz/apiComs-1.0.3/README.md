# winter-api-commons


This is a package to stremaline api method calls

This module containes the major reusable functions which can be imported and accessed directly which will reduce the time and code redundancy.

Installation
```
pip install apiCom
```


> Sample code:
```
import apiCom
url = "https://api.car.com/teslar/model1"
header = {}
resp = apiCom.get_api(url, header)
print(resp.json())
```

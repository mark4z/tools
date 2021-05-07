import json
from decimal import Decimal

import requests

url = "http://fundgz.1234567.com.cn/js/#{code}.js"

all = "31544.28"
codes = "519755,519718,519723,164902,519752,519782,519738,006793,008204,519772,519704,005001".split(",")
scale = "12.87, 12.81, 11.79, 11.79, 10.52, 9.80, 9.79, 5.92, 5.35, 4.11, 3.33, 1.29, 0.63".split(",")

ans = Decimal()
for i in range(len(codes)):
    c = codes[i]
    res = json.loads(requests.get(url.replace("#{code}", c)).text.replace("jsonpgz(", "").replace(");", ""))

    gszzl = Decimal(res['gszzl'])
    hold = Decimal(scale[i])
    q = (gszzl / 100) * (hold / 100)

    print(f'{gszzl:+}', hold, f'{q:+}', res['name'], res['gztime'])
    ans += q
print(ans, Decimal(all) * ans)

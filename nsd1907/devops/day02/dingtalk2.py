import requests
import getpass
import json

data = {
     "msgtype": "markdown",
     "markdown": {
         "title": "杭州天气",
         "text": "## 杭州天气 @156xxxx8827\n" +
                 "> 9度，西北风1级，空气良89，相对温度73% 少壮不努力\n\n" +
                 "> ![screenshot](https://img03.sogoucdn.com/app/a/100520021/ddc50ce5c94212c2ab3b70c16e419e62)\n" +
                 "> #### 10点20分发布 [天气](http://fanyi.sogou.com/) \n"
     },
     "at": {
        "atMobiles": [
            # "156xxxx8827",
            # "189xxxx8325"
        ],
        "isAtAll": False
    }
}


url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

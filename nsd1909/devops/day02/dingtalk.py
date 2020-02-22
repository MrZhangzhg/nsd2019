import requests
import json
import getpass

url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "宅家学习。我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {
#         "atMobiles": [],    # @哪些人
#         "isAtAll": False  # 是否@所有人
#     }
# }

# data = {
#     "msgtype": "link",
#     "link": {
#         "text": """宅家学习。这个即将发布的新版本，创始人xx称它为“红树林”。
# 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？""",
#         "title": "时代的火车向前开",
#         "picUrl": "http://world.people.com.cn/NMediaFile/2020/0217/MAIN202002171833000070170686703.JPG",
#         "messageUrl": "http://www.sogou.com"
#     }
# }

data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text": "#### 杭州天气 @156xxxx8827\n" +
                 "> 9度，西北风1级，空气良89，相对温度73% 宅家学习\n\n" +
                 "> ![screenshot](http://world.people.com.cn/NMediaFile/2020/0217/MAIN202002171833000070170686703.JPG)\n"  +
                 "> ###### 10点20分发布 [天气](http://fanyi.sogou.com/) \n"
    },
    "at": {
        "atMobiles": [
            "156xxxx8827",
            "189xxxx8325"
        ],
        "isAtAll": False
    }
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

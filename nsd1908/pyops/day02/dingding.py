import requests
import getpass
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827好好学习天天向上"
#     },
#     "at": {  # @哪些人
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False  # @所有人
#     }
# }

# data = {
#     "msgtype": "link",
#     "link": {
#         "text": """这个即将发布的新版本，创始人xx称它为“红树林”。
# 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？好好学习天天向上""",
#         "title": "时代的火车向前开",
#         "picUrl": "https://img03.sogoucdn.com/app/a/07/f13b5c3830f02b6db698a2ae43ff6a67",
#         "messageUrl": "http://pic.sogou.com"
#     }
# }

data = {
     "msgtype": "markdown",
     "markdown": {
         "title": "春节放假通知",
         "text": "## 2020年春节放假安排\n" +
                 "> 共放假7天，好好学习天天向上" +
                 "> ![春节放假](http://5b0988e595225.cdn.sohucs.com/images/20200109/ee95514274fa420899f45bd60894eb5d.jpeg)\n"  +
                 "> ##### 2020年1月15日发布 [春节放假通知](https://www.sohu.com/a/365695294_120427283) \n"
     },
    "at": {
        "atMobiles": [
            "156xxxx8827",
            "189xxxx8325"
        ],
        "isAtAll": False
    }
 }


# url是钉钉机器人webhook地址
url = getpass.getpass()
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

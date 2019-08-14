import requests
import json
import getpass

url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",   # 文本消息
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827 nsd1903"
#     },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
data = {
    "msgtype": "link",
    "link": {
        "text": """这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。
而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？""",
        "title": "时代的火车向前开",
        "picUrl": "http://img03.sogoucdn.com/v2/thumb/resize/w/640/t/2/retype/ext/jpg/q/75?appid=200556&url=http%3A%2F%2Fimg03.sogoucdn.com%2Fapp%2Fa%2F200841%2F38fba83050849149921702a35451022c",
        "messageUrl": "http://pic.sogou.com"
    }
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

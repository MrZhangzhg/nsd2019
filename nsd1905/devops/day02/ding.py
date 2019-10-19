import requests
import json
import getpass

url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827"  # 消息正文
#     },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",   # @哪些人
#             "189xxxx8325"
#         ],
#         "isAtAll": False   # 是否@所有人
#     }
# }
# data = {
#     "msgtype": "link",
#     "link": {
#         "text": "这个即将发布的新版本，创始人xx称它为“红树林”",
#         "title": "时代的火车向前开",
#         "picUrl": "https://img02.sogoucdn.com/app/a/100520021/8448941d79bb0542d65d3c8ca3f62bc0",
#         "messageUrl": "http://fanyi.sogou.com"
#     }
# }

data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"杭州天气",
         "text": "#### 杭州天气 @156xxxx8827\n" +
                 "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
                 "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
                 "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
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
print(r.json())  # 打印返回信息

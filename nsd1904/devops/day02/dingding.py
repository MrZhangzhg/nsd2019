import getpass
import requests
import json

# 按要求修改请求头
headers = {'Content-Type': 'application/json;charset=utf-8'}
# 在阿里巴巴钉钉开放平台上把数据格式复制过来
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "你好，nsd1904测试"
#     },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }

# data = {
#     "msgtype": "link",
#     "link": {
#         "text": "devops是development和opations的结合",
#         "title": "nsd1904 python",
#         "picUrl": "https://img01.sogoucdn.com/app/a/100520021/09e16c260f901c78c70df448a142efd6",
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

# url是你群聊机器人的webhook地址
url = getpass.getpass()
# 发送post请求
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

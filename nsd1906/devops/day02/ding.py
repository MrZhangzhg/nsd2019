import requests
import json
import getpass

url = getpass.getpass()
# 头部固定的，钉钉开发者手册上明确要求的
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data是从钉钉开发者手册上粘过来的
# data = {
#     "msgtype": "text",
#     "text": {
#         "content": "天王盖地虎。我就是我, 是不一样的烟火@156xxxx8827"
#     },
#     "at": {
#         "atMobiles": [  # @哪些人
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False  # 是否@所有人
#     }
# }

data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "杭州天气",
        "text": "#### 杭州天气 @156xxxx8827\n" +
                "> 9度，西北风1级，空气良89，相对温度73% 天王盖地虎\n\n" +
                "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n"  +
                "> ###### 10点20分发布 [天气](http://www.sogou.com/) \n"
    },
    "at": {
        "atMobiles": [
            "156xxxx8827",
            "189xxxx8325"
        ],
        "isAtAll": False
    }
}

# 钉钉开发者手册明确要求，使用post方法
# 字典不能直接发送，必须转成json字符串
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())


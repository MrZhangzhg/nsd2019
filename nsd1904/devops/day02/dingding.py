import getpass
import requests
import json

# 按要求修改请求头
headers = {'Content-Type': 'application/json;charset=utf-8'}
# 在阿里巴巴钉钉开放平台上把数据格式复制过来
data = {
    "msgtype": "text",
    "text": {
        "content": "你好，nsd1904测试"
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

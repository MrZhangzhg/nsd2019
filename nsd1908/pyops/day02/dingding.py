import requests
import getpass
import json

headers = {'Content-Type': 'application/json;charset=utf-8'}
data = {
    "msgtype": "text",
    "text": {
        "content": "我就是我, 是不一样的烟火@156xxxx8827好好学习天天向上"
    },
    "at": {  # @哪些人
        "atMobiles": [
            "156xxxx8827",
            "189xxxx8325"
        ],
        "isAtAll": False  # @所有人
    }
}


# url是钉钉机器人webhook地址
url = getpass.getpass()
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

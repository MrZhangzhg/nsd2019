import requests
import getpass
import json

data = {
    "msgtype": "text",
    "text": {
        "content": "我就是我, 是不一样的烟火@156xxxx8827。少壮不努力力，老大徒伤悲"
    },
    "at": {   # @某人
        "atMobiles": [
            "156xxxx8827",
            "189xxxx8325"
        ],
        "isAtAll": False  # @所有人
    }
}

url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

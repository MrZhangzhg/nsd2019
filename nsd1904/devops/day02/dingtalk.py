import getpass
import requests
import json
import sys

def dingtalk(url, content, mobiles, atall=False):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": mobiles,
            "isAtAll": atall
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = getpass.getpass()
    content = sys.argv[1]
    mobiles = ['15098765678']
    result = dingtalk(url, content, mobiles)
    print(result)


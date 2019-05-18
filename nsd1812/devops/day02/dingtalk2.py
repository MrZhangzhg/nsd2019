import json
import requests
import getpass

def send_msg(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
    "msgtype": "link",
    "link": {
        "text": "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？",
        "title": "时代的火车向前开",
        "picUrl": "",
        "messageUrl": "http://www.sogou.com"
    }
}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    reminders = ['15055667788']  # 特殊提醒要查看的人,就是@某人一下
    url = getpass.getpass()
    print(send_msg(url))

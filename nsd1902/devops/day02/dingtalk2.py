import json
import requests
import getpass

url = getpass.getpass()
headers = {'Content-Type': 'application/json;charset=utf-8'}
# data = {
#     "msgtype": "link",
#     "link": {
#         "text": "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。"
#                 "而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？",
#         "title": "时代的火车向前开",
#         "picUrl": "https://upload.jianshu.io/collections/images/1647427/WechatIMG13.jpeg",
#         "messageUrl": "http://fanyi.sogou.com"
#     }
# }
# data = {
#      "msgtype": "markdown",
#      "markdown": {
#          "title":"杭州天气",
#          "text": "#### 杭州天气 @156xxxx8827\n" +
#                  "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
#                  "> ![screenshot](https://gw.alipayobjects.com/zos/skylark-tools/public/files/84111bbeba74743d2771ed4f062d1f25.png)\n"  +
#                  "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
#      },
#     "at": {
#         "atMobiles": [
#             "156xxxx8827",
#             "189xxxx8325"
#         ],
#         "isAtAll": False
#     }
# }
data = {
    "actionCard": {
        "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
        "text": """![screenshot](https://upload.jianshu.io/collections/images/1647427/WechatIMG13.jpeg) 
 ### 乔布斯 20 年前想打造的苹果咖啡厅 
 Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划""",
        "hideAvatar": "0",
        "btnOrientation": "0",
        "singleTitle" : "阅读全文",
        "singleURL" : "https://www.dingtalk.com/"
    },
    "msgtype": "actionCard"
}
r = requests.post(url, data=json.dumps(data), headers=headers)

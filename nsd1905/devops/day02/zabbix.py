import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###############################################
# 查看非隐私信息，不需要认证，可以直接获取
data = {
    "jsonrpc": "2.0",   # zabbix使用的协议，固定值
    "method": "apiinfo.version",  # 获取软件版本的方法
    "params": [],   # 参数
    "id": 1   # 随便填一个数字，表示作业号
}

###############################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回的消息，主要关注result即可


import json
import requests

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
####################################################
# 对于非隐私数据，可以直接请求
data = {
    "jsonrpc": "2.0",   # jsonrpc版本，固定的
    "method": "apiinfo.version",  # 获取zabbix版本的方法
    "params": [],  # 参数
    "id": 101  # 随便写个数字，表示任务号
}


####################################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())   # 主要看result的值


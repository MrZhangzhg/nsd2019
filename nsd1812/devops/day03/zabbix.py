import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################
# 获取zabbix api版本信息
data = {
    "jsonrpc": "2.0",  # zabbix固定值
    "method": "apiinfo.version",   # 官方手册页上查询到的
    "params": [],  # 参数
    "id": 101  # 作业ID，随便指定一个值即可
}
###################################


###################################
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json())

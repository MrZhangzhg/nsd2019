import requests
import json

url = 'http://192.168.113.133/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
#####################################
# 获取zabbix版本
data = {
    "jsonrpc": "2.0",              # jsonrpc版本
    "method": "apiinfo.version",   # 使用的方法
    "params": [],                  # 参数
    "id": 1                        # 随便给定一个数字，表示作业号
}



#####################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回的数据只关心result内容

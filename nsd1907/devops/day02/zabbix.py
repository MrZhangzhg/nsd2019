import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
##################################
# 如果获取的是公开数据，可以直接取
data = {
    "jsonrpc": "2.0",  # jsonprc协议版本，固定的
    "method": "apiinfo.version",  # 请求方法，官方手册上查询
    "params": [],   # 参数
    "id": 100   # 随便给一个数字，表示任务号
}
##################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要看result部分

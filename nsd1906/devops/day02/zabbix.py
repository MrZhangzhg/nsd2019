import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}

#############################
# 如果获取公共信息，可以直接发请求，如软件版本
data = {
    "jsonrpc": "2.0",  # zabbix采用jsonrpc协议，固定值
    "method": "apiinfo.version",  # 方法
    "params": [],  # 参数
    "id": 101  # 随意给一个数字，表示作业号
}


#############################
# 输出内容，主要关注result即可
r = requests.post(url, headers=header, data=json.dumps(data))
print(r.json())

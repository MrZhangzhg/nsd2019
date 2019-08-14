import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################
# 有些数据不需权限，可以直接获取，如版本号
# 查看结果，主要看result的值
data = {
    "jsonrpc": "2.0",   # 固定值
    "method": "apiinfo.version",
    "params": [],   # 参数
    "id": 101   # 随便填一个数字，表示任务ID
}


###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

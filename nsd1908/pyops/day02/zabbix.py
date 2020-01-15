import json
import requests

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json'}
##############################
# 获取版本号，不需要认证，可以直接请求
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],  # 参数
#     "id": 101  # 随便给定一个数字，表示作业号
# }
##############################
# 获取admin用户的token, 7233c34f9178cbedd0bf45eabe545b6f
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
##############################
# 取出全部的用户
data = {
    "jsonrpc": "2.0",
    "method": "user.get",
    "params": {
        "output": "extend"
    },
    "auth": "7233c34f9178cbedd0bf45eabe545b6f",
    "id": 1
}


r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要获取result相关信息

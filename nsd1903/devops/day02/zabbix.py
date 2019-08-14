import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################
# 有些数据不需权限，可以直接获取，如版本号
# 查看结果，主要看result的值
# data = {
#     "jsonrpc": "2.0",   # 固定值
#     "method": "apiinfo.version",
#     "params": [],   # 参数
#     "id": 101   # 随便填一个数字，表示任务ID
# }
###################################
# 有些数据，必须授权后才能获取，授权使用令牌
# 获取令牌
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 37852e5313817edc8dd5812ddb8064f8
###################################
# 获取所有的主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤，仅获取某几台主机信息
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "37852e5313817edc8dd5812ddb8064f8",
#     "id": 1
# }
####################################
# 删除id为10257的主机
data = {
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [
        "10257",
        # "32"
    ],
    "auth": "37852e5313817edc8dd5812ddb8064f8",
    "id": 1
}




###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

import json
import requests

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
####################################################
# 对于非隐私数据，可以直接请求
# data = {
#     "jsonrpc": "2.0",   # jsonrpc版本，固定的
#     "method": "apiinfo.version",  # 获取zabbix版本的方法
#     "params": [],  # 参数
#     "id": 101  # 随便写个数字，表示任务号
# }
####################################################
# 获取隐私数据，首先要进行认证，能过认证得到用户的token
# 16534fe5f385c05ef05c1d3e36afb4d9
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
####################################################
# 获取所有的主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
#     "id": 1
# }
# 'hostid': '10259',
####################################################
# 删除主机
data  = {
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [
        "10259",   # 待删除主机的ID号
    ],
    "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
    "id": 1
}




####################################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())   # 主要看result的值


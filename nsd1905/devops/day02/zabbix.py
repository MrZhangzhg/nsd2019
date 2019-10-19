import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###############################################
# 查看非隐私信息，不需要认证，可以直接获取
# data = {
#     "jsonrpc": "2.0",   # zabbix使用的协议，固定值
#     "method": "apiinfo.version",  # 获取软件版本的方法
#     "params": [],   # 参数
#     "id": 1   # 随便填一个数字，表示作业号
# }
###############################################
# 查看隐私信息需要认证，通过用户名和密码获取token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# b6ffc95ac791b368d9ba12d45f2c2edb
###############################################
# 获取主机信息, 'hostid': '10260'
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤满足条件的主机
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#             ]
#         }
#     },
#     "auth": "b6ffc95ac791b368d9ba12d45f2c2edb",
#     "id": 1
# }
###############################################
# 删除主机
data = {
    "jsonrpc": "2.0",
    "method": "host.delete",
    "params": [
        "10260",
        # "32"
    ],
    "auth": "b6ffc95ac791b368d9ba12d45f2c2edb",
    "id": 1
}


###############################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回的消息，主要关注result即可


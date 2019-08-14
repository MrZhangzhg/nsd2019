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
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10257",
#         # "32"
#     ],
#     "auth": "37852e5313817edc8dd5812ddb8064f8",
#     "id": 1
# }
###################################
# 获取Linux Servers组的ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "37852e5313817edc8dd5812ddb8064f8",
#     "id": 1
# }
# group-id: 2
###################################
# 获取Template OS Linux模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "37852e5313817edc8dd5812ddb8064f8",
#     "id": 1
# }
# tid: 10001
###################################
# 创建主机nsd1903web1，加入Linux servers组，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1903web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.6",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "sfdalsfdaljk",
            "macaddress_b": "56768"
        }
    },
    "auth": "37852e5313817edc8dd5812ddb8064f8",
    "id": 1
}



###################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

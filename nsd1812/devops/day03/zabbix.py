import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################
# 获取zabbix api版本信息
# data = {
#     "jsonrpc": "2.0",  # zabbix固定值
#     "method": "apiinfo.version",   # 官方手册页上查询到的
#     "params": [],  # 参数
#     "id": 101  # 作业ID，随便指定一个值即可
# }
###################################
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
# 99845118dd0855dcc0eafdb94d6175ca
###################################
# 获取主机信息
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
#     "auth": "99845118dd0855dcc0eafdb94d6175ca",
#     "id": 1
# }
###################################
# 删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10255",
#     ],
#     "auth": "99845118dd0855dcc0eafdb94d6175ca",
#     "id": 1
# }
###################################
# 取出Linux Servers组号
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "99845118dd0855dcc0eafdb94d6175ca",
#     "id": 1
# }
# groupid: 2
###################################
# 取出Template OS Linux模板的ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": "99845118dd0855dcc0eafdb94d6175ca",
#     "id": 1
# }
# 'templateid': '10001'
###################################
# 创建主机
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1812web1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.2",
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
            "macaddress_a": "123456789012",
            "macaddress_b": "fsdalkjfsdaljfdsa"
        }
    },
    "auth": "99845118dd0855dcc0eafdb94d6175ca",
    "id": 1
}



###################################
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.json())

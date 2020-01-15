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
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {
#         "output": "extend"
#     },
#     "auth": "7233c34f9178cbedd0bf45eabe545b6f",
#     "id": 1
# }
##############################
# 获取主机信息, 'hostid': '10264',
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤出指定条件的主机
#             "host": []
#         }
#     },
#     "auth": "7233c34f9178cbedd0bf45eabe545b6f",
#     "id": 1
# }
##############################
# 删除hostid为10264的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10264"
#     ],
#     "auth": "7233c34f9178cbedd0bf45eabe545b6f",
#     "id": 1
# }
##############################
# 获取组信息, 'groupid': '2', 'name': 'Linux servers',
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
#     "auth": "7233c34f9178cbedd0bf45eabe545b6f",
#     "id": 1
# }


##############################
# 获取模板信息, 'templateid': '10001'
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
#     "auth": "7233c34f9178cbedd0bf45eabe545b6f",
#     "id": 1
# }


##############################
# 创建nsd1908web1主机，它在Linux servers组中，应用Template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1908web1",
        "interfaces": [  # 定义监控的方式，使用agent
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.254",
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
        "inventory_mode": 0,  # 主机资产记录
        "inventory": {
            "macaddress_a": "asdfjklasdfjklasdf",
            "macaddress_b": "789235789023"
        }
    },
    "auth": "7233c34f9178cbedd0bf45eabe545b6f",
    "id": 1
}


r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 主要获取result相关信息

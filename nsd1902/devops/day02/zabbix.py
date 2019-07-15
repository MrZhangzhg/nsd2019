import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers	= {'Content-Type': 'application/json-rpc'}
########################################
# 获取zabbix版本信息
# data = {
#     "jsonrpc": "2.0",   # 固定值
#     "method": "apiinfo.version",  # 根据需求查手册获得
#     "params": [],   # 参数
#     "id": 101   # 随便给一个数字，表示任务编号
# }
########################################
# 获取管理员的token，将来通过token访问需要权限的资源
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 3d1cdc23a9304a0bd261c92ca75f80c7
########################################
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
#     "auth": "3d1cdc23a9304a0bd261c92ca75f80c7",
#     "id": 1
# }
########################################
# 删除id为10256的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10256",
#     ],
#     "auth": "3d1cdc23a9304a0bd261c92ca75f80c7",
#     "id": 1
# }
########################################
# 获取Linux servers组信息
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
#     "auth": "3d1cdc23a9304a0bd261c92ca75f80c7",
#     "id": 1
# }
# groupid: 2
########################################
# 获取Template OS Linux模板信息
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
#     "auth": "3d1cdc23a9304a0bd261c92ca75f80c7",
#     "id": 1
# }
# 'templateid': '10001'
########################################
# 创建名为nsd1902web1的主机，属于Linux Servers组，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1902web1",
        "interfaces": [   # 指定通过什么方式进行监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"   # zabbix agent方式
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
        "inventory_mode": 0,   # 配置主机资产清单，如，用于资产盘查
        "inventory": {
            "macaddress_a": "abcdxyz",
            "macaddress_b": "56768"
        }
    },
    "auth": "3d1cdc23a9304a0bd261c92ca75f80c7",
    "id": 1
}


########################################

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

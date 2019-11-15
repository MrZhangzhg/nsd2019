import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}

#############################
# 如果获取公共信息，可以直接发请求，如软件版本
# data = {
#     "jsonrpc": "2.0",  # zabbix采用jsonrpc协议，固定值
#     "method": "apiinfo.version",  # 方法
#     "params": [],  # 参数
#     "id": 101  # 随意给一个数字，表示作业号
# }
#############################
# 通过用户名和密码获取认证令牌
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 51363d1c6b9a3f0579c8a2b34821909e
#############################
# 获取所有的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤出符合条件的主机
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "51363d1c6b9a3f0579c8a2b34821909e",
#     "id": 1
# }
#############################
# 删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10261",  # 删除主机id是10261的主机
#     ],
#     "auth": "51363d1c6b9a3f0579c8a2b34821909e",
#     "id": 1
# }
#############################
# 获取Linux Servers组的ID => 2
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
#     "auth": "51363d1c6b9a3f0579c8a2b34821909e",
#     "id": 1
# }
#############################
# 获取Template OS Linux的ID =>10001
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
#     "auth": "51363d1c6b9a3f0579c8a2b34821909e",
#     "id": 1
# }
##############################
# 创建名nsd1906web1的主机，它在Linux Servers组中，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1906web1",
        "interfaces": [   # 通过什么方式监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.100",
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
        "inventory_mode": 0,   # 主机资产记录
        "inventory": {
            "macaddress_a": "mei you",
            "macaddress_b": "56768"
        }
    },
    "auth": "51363d1c6b9a3f0579c8a2b34821909e",
    "id": 1
}





#############################
# 输出内容，主要关注result即可
r = requests.post(url, headers=header, data=json.dumps(data))
print(r.json())

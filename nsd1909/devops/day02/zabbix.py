import requests
import json

url = 'http://192.168.113.133/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
#####################################
# 获取zabbix版本
# data = {
#     "jsonrpc": "2.0",              # jsonrpc版本
#     "method": "apiinfo.version",   # 使用的方法
#     "params": [],                  # 参数
#     "id": 1                        # 随便给定一个数字，表示作业号
# }
#####################################
# 获取其他隐私数据，需要认证。认证时采用令牌的形式
# 1e3972f1bf319cf35ea4bd8cc22f043b
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
#####################################
# 获取所有监控的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#             ]
#         }
#     },
#     "auth": "1e3972f1bf319cf35ea4bd8cc22f043b",
#     "id": 1
# }
#####################################
# 获取Linux servers组id  -> 2
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
#     "auth": "1e3972f1bf319cf35ea4bd8cc22f043b",
#     "id": 1
# }
#####################################
# 获取Template OS Linux模板id  -> 10001
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
#     "auth": "1e3972f1bf319cf35ea4bd8cc22f043b",
#     "id": 1
# }
#####################################
# 创建一台监控主机名为nsd1909web1，它在Linux servers组中，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1909web1",
        "interfaces": [   # 使用哪种方法进行监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.113.1",
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
            "macaddress_a": "01234asdfasdf",
            "macaddress_b": "56768234aljfieri23jlf"
        }
    },
    "auth": "1e3972f1bf319cf35ea4bd8cc22f043b",
    "id": 1
}




#####################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回的数据只关心result内容

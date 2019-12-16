import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
##################################
# 如果获取的是公开数据，可以直接取
# data = {
#     "jsonrpc": "2.0",  # jsonprc协议版本，固定的
#     "method": "apiinfo.version",  # 请求方法，官方手册上查询
#     "params": [],   # 参数
#     "id": 100   # 随便给一个数字，表示任务号
# }
##################################
# 非公开数据，需要合法用户。合法用户通过token令牌验证
# 获取令牌 -> 5577e6f88fbbc718a749d714ed9da3a9
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
##################################
# 获取所有的主机信息，找到主机的hostid
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
#     "auth": "5577e6f88fbbc718a749d714ed9da3a9",  # 令牌
#     "id": 1
# }
##################################
# 删除id为10262的主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10262",  # 待删除的主机的id
#     ],
#     "auth": "5577e6f88fbbc718a749d714ed9da3a9",
#     "id": 1
# }
##################################
# 获取模板id > 10001
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
#     "auth": "5577e6f88fbbc718a749d714ed9da3a9",
#     "id": 1
# }

##################################
# 获取组id > 2
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
#     "auth": "5577e6f88fbbc718a749d714ed9da3a9",
#     "id": 1
# }

##################################
# 创建nsd1907web1主机，将它加到Linux Servers组中
# 应用Template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1907web1",
        "interfaces": [   # 用哪种方式监控主机
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.5",
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
            "macaddress_a": "zfasdfjklfsd",
            "macaddress_b": "asdfjklafsd23890"
        }
    },
    "auth": "5577e6f88fbbc718a749d714ed9da3a9",
    "id": 1
}



##################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要看result部分

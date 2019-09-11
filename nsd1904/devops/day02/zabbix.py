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
# data  = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10259",   # 待删除主机的ID号
#     ],
#     "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
#     "id": 1
# }
####################################################
# 获取Linux Servers组的信息
# 'groupid': '2'
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
#     "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
#     "id": 1
# }
####################################################
# 获取Template OS Linux模板信息
# 'templateid': '10001'
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
#     "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
#     "id": 1
# }
####################################################
# 创建主机，名为nsd1904web1，加入到Linux Servers组，
# 应用Template OS Linux模板
data  = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "nsd1904web1",  # 主机名
        "interfaces": [  # 使用zabbix agent进行监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.5",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [  # 加入的组
            {
                "groupid": "2"
            }
        ],
        "templates": [   # 应用的模板
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,  # 资产清单
        "inventory": {
            "macaddress_a": "mac addr 1",
            "macaddress_b": "56768"
        }
    },
    "auth": "16534fe5f385c05ef05c1d3e36afb4d9",
    "id": 1
}

####################################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())   # 主要看result的值


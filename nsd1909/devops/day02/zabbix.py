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
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                # "Zabbix server",
                # "Linux server"
            ]
        }
    },
    "auth": "1e3972f1bf319cf35ea4bd8cc22f043b",
    "id": 1
}

#####################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回的数据只关心result内容

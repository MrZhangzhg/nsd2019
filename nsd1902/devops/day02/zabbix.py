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
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}
# 3d1cdc23a9304a0bd261c92ca75f80c7
########################################

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())

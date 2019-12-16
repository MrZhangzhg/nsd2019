# nsd1907_devops_day02

## 邮件编程

- 发邮件时，两件事：准备邮件、发送邮件
- 准备邮件使用email模块
- 发送邮件使用smtplib模块

## JSON

- JSON(JavaScript Object Notation)
- JSON采用完全独立于语言的文本格式
- JSON成为理想的数据交换语言

```python
>>> import json
>>> adict = {'name': 'tom', 'age': 20}
>>> data = json.dumps(adict)  # 将字典转成json字符串
>>> type(data)
<class 'str'>
>>> data
'{"name": "tom", "age": 20}'
>>> len(data)
26
>>> jdata = json.loads(data)  # 将json字符串转成python数据类型
>>> type(jdata)
<class 'dict'>
>>> jdata
{'name': 'tom', 'age': 20}
>>> len(jdata)
2
```

天气预报查询：

实况天气：http://www.weather.com.cn/data/sk/城市代码.html

城市信息：http://www.weather.com.cn/data/cityinfo/城市代码.html

详细指数：http://www.weather.com.cn/data/zs/城市代码.html

在搜索引擎中输入“中国天气网城市代码”搜索城市代码

## requests模块

- Requests是用Python语言编写的、优雅而简单的HTTP库
- Requests内部采用来urillib3
- requests模块，将HTTP的方法定义好了与之对应的函数。需要使用什么方法访问URL，只要调用相关的函数即可。
- HTTP GET方法
  - 在浏览器的网址中书写url进行访问
  - 点击页面中的超链接
  - 有些表单的搜索
- HTTP POST方法：通过表单提交(隐私)数据，如登陆、注册

```python
(nsd1907) [root@room8pc16 day02]# pip install /var/ftp/pub/zzg_pypkgs/requests_pkgs/*
>>> import requests
>>> r = requests.get('http://www.163.com')
>>> r.text  # 文本内容使用r.text方法获取

>>> r = requests.get('https://i02picsos.sogoucdn.com/57bb0cff2c3d1a0e')
>>> r.content   # 非文本内容，使用r.content获取
>>> with open('/tmp/a.jpg', 'wb') as fobj:
...   fobj.write(r.content)
(nsd1907) [root@room8pc16 day02]# eog /tmp/a.jpg 

>>> url = 'http://www.weather.com.cn/data/zs/101010100.html'
>>> r = requests.get(url)
>>> r.json()   # 此时为乱码
>>> r.encoding  # 查看当前字符编码
'ISO-8859-1'
>>> r.encoding = 'utf8'   # 修改编码
>>> r.json()
```

查快递

- url: http://www.kuaidi100.com/query?type=%s&postid=%s
  - ?左边部分是url
  - ?右边部分是传给url的参数

```python
>>> url = 'http://www.kuaidi100.com/query'
>>> params = {'type': 'youzhengguonei', 'postid': '9897314440481'}
>>> r = requests.get(url, params=params)
>>> r.json()
```

## 钉钉机器人的实现

- https://www.jianshu.com/p/a3c62eb71ae3
- 创建一个群聊机器人。通过python让机器人在群中说话



### 图灵机器人

- https://www.jianshu.com/p/3c0436af6e92

```python
zhangzhigangdeMacBook-Pro: zhangzhigang$ vim tuling_robot.py
import requests
import json

def tuling_reply(url, apikey, msg):
    data = {     # 这个是在帮助手册上直接复制过来的
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "天坛北门"
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,      # 你注册的apikey
            "userId": "anystr"      # 随便填点
        }
    }
    headers = {'content-type': 'application/json'}     # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    apikey = '填入机器人的apikey'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    while True:
        msg = input('(输入quit结束)> ').strip()
        if not msg:
            continue
        if msg == 'quit':
            break
        reply = tuling_reply(url, apikey, msg)
        print(reply["results"][0]["values"]["text"])    # 可以直接打印reply
```

### 接入微信的模块：itchat

## zabbix编程

- api：应用程序编程接口

- zabbix网页拷贝到了web目录下，起名为zabbix，则zabbix的api地址就是：

  http://xxx.xxx/zabbix/api_jsonrpc.php

- zabbix中文官方文档页：https://www.zabbix.com/documentation/3.4/zh/manual












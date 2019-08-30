f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/list', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
###################################
# 问题1: 建议用变量代替字面量
# 问题2：文件对象名f1/f2没有含义
# 问题3：读取文件全部内容可能读入量太大


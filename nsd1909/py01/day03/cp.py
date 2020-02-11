# 当前代码的问题：
# 1. 源和目录文件都是直接写的字面量，建议改为变量
# 2. f1/f2这样的变量没有意义，建议改为有意义的名字
# 3. read默认读取全部内容，应该一次少读取一些数据，读多次

f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

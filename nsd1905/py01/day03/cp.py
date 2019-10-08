f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

# 程序需要改进的地方
# 尽量使用变量，不要直接使用字面量
# 变量名应该有意义
# 如果文件很大，一次把所有内容读取出来，会占用太多的内存空间

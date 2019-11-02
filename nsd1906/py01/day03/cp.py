# 代码问题：
# 不建议硬编码，把文件路径用变量表示
# 变量名应该有意义
# 如果文件很大，将会占有太多的内存

f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/list', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

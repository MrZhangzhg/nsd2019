# 以下写法，可以工作，但是不好。如果源文件很大，数据读取出来赋值给data，data
# 将会消耗大量的内存

with open('/bin/ls', 'rb') as f1:
    data = f1.read()

with open('/tmp/list', 'wb') as f2:
    f2.write(data)

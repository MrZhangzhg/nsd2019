import shutil

# f1 = open('/etc/hosts', 'rb')
# f2 = open('/tmp/zhuji', 'wb')
# shutil.copyfileobj(f1, f2)
# f1.close()
# f2.close()

# shutil.copy('/etc/hosts', '/tmp/')   # 常用
# shutil.move('/tmp/hosts', '/tmp/zhuji.txt')  # mv
# shutil.copytree('/etc/security', '/tmp/anquan')  # cp -r
# shutil.rmtree('/tmp/anquan')   # rm -rf

alist = ['tom', 'jerry', 'bob', 'alice']
for i in range(len(alist)):
    print('%s: %s' % (i, alist[i]))

for item in enumerate(alist):
    print('%s: %s' % item)

for ind, name in enumerate(alist):
    print('%s: %s' % (ind, name))








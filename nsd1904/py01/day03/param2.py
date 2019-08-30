def show(content):
    # 将列表中的内容加上行号输出
    for i in range(len(content)):
        print("%s: %s" % (i, content[i]))


# alist = []
# while True:
#     data = input('(end to quit)> ')
#     if data == 'end':
#         break
#
#     alist.append(data)
fobj = open('/etc/postfix/main.cf')
alist = fobj.readlines()
fobj.close()
show(alist)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print('hello', end=' ')
#     print()

# print默认在结尾打印回车，可以通过end替换为其他字符
# 外层循环控制第几行，内层循环控制一行内打印多少次

# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print('hello', end=' ')
#     print()


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()

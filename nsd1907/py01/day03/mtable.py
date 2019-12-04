# for i in range(1, 4):  # 控制第几行的打印
#     # 每行之内再循环打印3个hello
#     for j in range(1, 4):   # 行内重复打印3个hello
#         print('hello', end=' ')  # print默认在结尾打印回车，改为空格
#     print()  # 每行结尾打印回车

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # print('*', end='')
#         print('hello', end=' ')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()


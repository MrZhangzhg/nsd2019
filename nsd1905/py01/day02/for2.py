# for i in range(1, 6):
#     print('i:', i)
#     for j in range(1, 6):
#         print('j:', j, end=' ')  # print默认在结尾打印回车，用end改为空格
#     print()   # 打印回车

for i in range(1, 10):  # [1, 2, 3....9]
    for j in range(1, i + 1):   # [1, 2, 3....9]
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()



# for i in range(3):
#     for j in range(3):
#         print('hello', end=' ')  # print默认在结尾打印\n，改为空格
#     print()  # 打印回车


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('hello', end=' ')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()

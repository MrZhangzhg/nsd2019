# for i in range(3):
#     print('hello')

# for i in range(3):   # 控制第几行
#     for j in range(3):   # 控制行内打印的次数
#         print('hello')


# for i in range(3):   # 控制第几行
#     for j in range(3):   # 控制行内打印的次数
#         print('hello', end=' ')  # print默认最后打印回车，改为空格

# for i in range(3):   # 控制第几行
#     # 外层循环，打印3个hello，再打印一个回车
#     for j in range(3):   # 控制行内打印的次数
#         print('hello', end=' ')  # print默认最后打印回车，改为空格
#     print()   #  print默认最后打印回车


# i 取值 [0, 1, 2]
# i = 0  => j 取值 [0]
# i = 1  => j 取值 [0, 1]
# i = 2  => j 取值 [0, 1, 2]

# for i in range(3):   # 控制第几行
#     # 外层循环，打印3个hello，再打印一个回车
#     for j in range(i + 1):   # 控制行内打印的次数
#         print('hello', end=' ')  # print默认最后打印回车，改为空格
#     print()   #  print默认最后打印回车


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()

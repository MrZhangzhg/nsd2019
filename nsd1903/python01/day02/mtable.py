# for i in range(3):
#     print('hello')

# for i in range(3):  # [0, 1, 2]
    # 外层循环控制第几行，行内打印hello后，再打印回车
    # for j in range(3):  # [0, 1, 2]
        # print默认打印回车，可以通过end指定结束打印内容
        # print('hello', end=' ')
    # print()   # print默认打印回车
###################################

# for i in range(3):
#     for j in range(i + 1):
#         print('hello', end=' ')
#     print()
###################################
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%sx%s=%s' % (j, i, i * j), end=' ')
#     print()

###################################
for i in range(1, 10):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
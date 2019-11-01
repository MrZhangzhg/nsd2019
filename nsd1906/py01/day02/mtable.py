# i取值[1, 2, 3]
# i == 1，j取值[1, 2, 3]
# i == 2, j从新再取值[1, 2, 3]
# i == 3, j从新再取值[1, 2, 3]
# print默认会在结束打印换行，可以使用end=' '替换为空格
# 外层循环最后要打印换行
# for i in range(1, 4):  # 外层循环控制行数
#     for j in range(1, 4):  # 内层循环控制行内打印次数
#         print('hello', end=' ')
#     print()

# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print('hello', end=' ')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()

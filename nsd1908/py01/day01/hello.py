# print('Hello World!')
#
# if 3 > 0:
#     print('yes')
#     print('ok')

# a = 3; b = 4

# print('Hello World')  # 打印一个字符串
# 打印两个字符串和一个数字，输出结果默认各项之间用空格分隔
# print('hao', 'ya', 123)
# 可以通过sep指定分隔符
# print('hao', 'ya', 123, sep='***')
# 字符串使用+进行拼接，拼接的结果输出
# print('Hello' + 'World')
# print('hao' + 123)  # 错误，字符串与数字不能直接运算

n = input('number: ')   # input读入的数据一定为字符类型
print(n)

# print(n + 5)   # 不能直接将数字与字符串运算
print(int(n) + 5)  # int可将字符串形式的数字转换成整数数字
print(n + str(5))  # str可将任意类型的数据转换成字符串






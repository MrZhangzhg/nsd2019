# print("Hello World!")
#
# if 3 > 0:
#     print('yes')
#     print('ok')
#
# s = 'Hello World!' + \
#     'Hello tedu'
#
# a = 3; b = 4
# c = 5
# d = 6

# 打印一行字符串
# print('Hello World!')

# 字符串可以使用+进行拼接，拼接后再打印
# print('Hello' + 'World')

# print打印多项时，用逗号分开各项，默认各项间使用空格作为分隔符
# print('Hao', 123)

# 也可以通过sep指定分隔符
# print('Hao', 123, 'abc', 456)
# print('Hao', 123, 'abc', 456, sep='***')

# 字符串中间如果需要有变化的内容，可以使用%s占位，然后在字符串外边指定具体内容
# print('I am %s' % 'zzg')
# print('%s is %s years old.' % ('tom', 20))

# username = input('username: ')
# print(username)

# input读入的内容一定是字符类型
n = input('number: ')
# print(n + 10)   # 错误，不能把字符和数字进行运算
a = int(n) + 10   # int函数可以将字符串数字转换成整数
print(a)
b = n + str(10)   # str函数可以将对象转换成字符串
print(b)


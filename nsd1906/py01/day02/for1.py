s1 = 'hello'
nums = [10, 20, 15, 80]
names = ('tom', 'jerry')
user = {'name': 'bob', 'age': 20}
#
# for ch in s1:
#     print(ch)
#
# print('*' * 50)
# for i in nums:
#     print(i)
#
# print('*' * 50)
# for name in names:
#     print(name)
#
# print('*' * 50)
# for key in user:
#     print(key, user[key])


# for循环常与range连用
print(range(10))  # range只是一个对象，潜在可以生成很多数
# range没有给起始数字，从0开始。结束数字不包含
for i in range(10):
    print(i)

# 将range转换成列表再打印
print(list(range(10)))

# 打印6到10的列表
print(list(range(6, 11)))

print(list(range(1, 10, 2)))
print(list(range(10, 0, -1)))
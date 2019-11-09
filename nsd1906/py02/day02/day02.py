# def func1():
#     print('func 1')
#     func2()
#
# def func2():
#     print('func 2')
#
# if __name__ == '__main__':
#     func1()

from random import randint

def func1(x):
    return x % 2   # 结果只有1和0两种情况，1为真，0为假
    # return True if x % 2 == 1 else False

def func2(x):
    return x * 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    # result = filter(func1, nums)
    # print(list(result))
    # result2 = filter(lambda x: x % 2, nums)
    # print(list(result2))
    result3 = map(func2, nums)
    print(list(result3))
    result4 = map(lambda x: x * 2, nums)
    print(list(result4))














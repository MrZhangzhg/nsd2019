# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# if __name__ == '__main__':
#     func1()

from random import randint

def func1(x):
    return True if x % 2 == 1 else False

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    print(list(result))
    result2 = filter(lambda x: True if x % 2 == 1 else False, nums)
    print(list(result2))










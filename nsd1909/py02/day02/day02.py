from random import randint

def func1(x):
    '接受一个数字，奇数返回True，偶数返回False'
    return True if x % 2 == 1 else False

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    result2 = filter(lambda x: True if x % 2 == 1 else False, nums)
    print(list(result))
    print(list(result2))

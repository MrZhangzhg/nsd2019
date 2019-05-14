from random import randint

def func1(x):
    return True if x > 50 else False

def func2(x):
    return x + 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    # result = filter(func1, nums)
    # print(list(result))
    # result2 = filter(lambda x: True if x > 50 else False, nums)
    # print(list(result2))
    result = map(func2, nums)
    print(list(result))
    result2 = map(lambda x: x + 2, nums)
    print(list(result2))

from random import randint

def func1(x):
    return True if x > 50 else False

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    print(list(result))
    result2 = filter(lambda x: True if x > 50 else False, nums)
    print(list(result2))

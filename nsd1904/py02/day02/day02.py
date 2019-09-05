from random import randint

def func1(x):
    return True if x % 2 else False
    # if x % 2 == 1:
    #     return True
    # else:
    #     return False

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(list(filter(func1, nums)))
    print(list(filter(lambda x: True if x % 2 else False, nums)))
    print(list(map(func2, nums)))
    print(list(map(lambda x: x * 2 + 1, nums)))

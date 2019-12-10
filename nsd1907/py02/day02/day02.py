# def func1():
#     print('func1')
#     func2()
#
# def func2():
#     print('func2')
#
# if __name__ == '__main__':
#     func1()


# from random import randint
#
# def func1(x):
#     return True if x % 2 == 0 else False
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = filter(func1, nums)
#     result2 = filter(lambda x: True if x % 2 == 0 else False, nums)
#     print(list(result))
#     print(list(result2))


from random import randint

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = map(func2, nums)
    result2 = map(lambda x: x * 2 + 1, nums)
    print(list(result))
    print(list(result2))





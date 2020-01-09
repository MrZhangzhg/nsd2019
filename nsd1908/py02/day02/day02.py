# from random import randint
#
# def func1(x):
#     return True if x % 2 == 1 else False
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = filter(func1, nums)
#     print(list(result))
#     result1 = filter(lambda x: True if x % 2 == 1 else False, nums)
#     print(list(result1))

# from random import randint
#
# def func2(x):
#     return x * 2
#
# if __name__ == '__main__':
#     nums = [randint(1, 100) for i in range(10)]
#     print(nums)
#     result = map(func2, nums)
#     print(list(result))
#     result1 = map(lambda x: x * 2, nums)
#     print(list(result1))

def func1(x):
    if x == 1:
        return 1

    return x * func1(x - 1)
#          5 * func1(4)
#          5 * 4 * func1(3)
#          5 * 4 * 3 * func1(2)
#          5 * 4 * 3 * 2 * func1(1)
#          5 * 4 * 3 * 2 * 1

if __name__ == '__main__':
    result = func1(5)
    print(result)










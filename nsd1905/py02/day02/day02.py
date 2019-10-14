# def func1():
#     print('in func1')
#     func2()
#
# def func2():
#     print('in func2')
#
# if __name__ == '__main__':
#     func1()

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
#     result2 = filter(lambda x: True if x % 2 == 1 else False, nums)
#     print(list(result2))

#
# def func1(s):
#     return s + '.com'
#
# if __name__ == '__main__':
#     alist = ['qq', 'sohu', '163']
#     result = map(func1, alist)
#     print(list(result))
#     result2 = map(lambda s: s + '.com', alist)
#     print(list(result2))

def func(x):
    if x == 1:
        return 1

    return x * func(x - 1)

if __name__ == '__main__':
    print(func(5))


# def foo():
#     print('in foo')
#     bar()
#
# def bar():
#     print('in bar')
#
# foo()

def func1(x):
    if x == 1:
        return x
    return x * func1(x - 1)
         # 5 * func1(4)
         # 5 * 4 * func(3)
         # 5 * 4 * 3 * func(2)
         # 5 * 4 * 3 * 2 * func(1)
         # 5 * 4 * 3 * 2 * 1

print(func1(5))

# >>> result = 1
# >>> for i in range(1, 6):
# ...   result *= i



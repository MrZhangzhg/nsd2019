# def fib_func():
#     fib = [0, 1]
#
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     print(fib)
#
# a = fib_func()   # 函数默认返回None
# print(a)


def fib_func(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib   # 函数的运行结果，用关键字return返回

# a = fib_func()
# print(a)

for i in range(2, 20):
    print(fib_func(i))

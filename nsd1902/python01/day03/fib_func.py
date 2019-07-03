def fib_func():
    '函数定义时，不会执行函数体内的代码'
    fib = [0, 1]

    n = int(input('长度: '))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    print(fib)

fib_func()    # 函数调用时，将会执行函数体内的代码
fib_func()
fib_func()

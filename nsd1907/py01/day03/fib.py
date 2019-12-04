def mk_fib():
    fib = [0, 1]  # 函数内部的变量是局部变量，只能在函数内使用

    n = int(input('长度: '))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回的是fib代表的列表，而不是返回变量

a = mk_fib()  # 调用函数时，必须用()，调用函数就是执行函数内的代码
print(a)

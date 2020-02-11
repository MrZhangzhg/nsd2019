# 定义函数时，函数内的代码不会执行
def mk_fib():
    fib = [0, 1]

    n = int(input('长度: '))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回的是fib代表的列表，而不是返回fib变量

a = mk_fib()   # 调用函数，就是执行函数内的代码
b = [i + 2 for i in a]
print(b)

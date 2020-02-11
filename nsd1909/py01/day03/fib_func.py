# 定义函数时，函数内的代码不会执行
def mk_fib():
    fib = [0, 1]

    n = int(input('长度: '))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    print(fib)

mk_fib()   # 调用函数，就是执行函数内的代码
mk_fib()

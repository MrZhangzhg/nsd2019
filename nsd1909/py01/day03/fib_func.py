# 定义函数时，函数内的代码不会执行
def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回的是fib代表的列表，而不是返回fib变量

a = mk_fib(5)   # 调用函数，就是执行函数内的代码
print(a)

nums = [5, 8, 10, 20]
for i in nums:
    print(mk_fib(i))  # 传参时，把i代表的数字传给mk_fib()函数，不是传变量

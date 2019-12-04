def mk_fib(n):
    fib = [0, 1]  # 函数内部的变量是局部变量，只能在函数内使用

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回的是fib代表的列表，而不是返回变量

a = mk_fib(5)  # 调用函数时，必须用()，调用函数就是执行函数内的代码
b = [i * 2 for i in a]
print(b)
with open('/tmp/fib.txt', 'w') as fobj:
    # 需要把列表转成str字符串后再写入文件，否则报错
    fobj.write(str(a))

n = int(input('长度: '))
c = mk_fib(n)
print(c)

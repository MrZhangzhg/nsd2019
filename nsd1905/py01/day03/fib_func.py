def mk_fib(n):
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = mk_fib(5)  # [0, 1, 1, 2, 3]
print(a)
l = int(input('长度: '))
b = mk_fib(l)
print(b)
# alist = [i * 2 for i in a]
# print(alist)

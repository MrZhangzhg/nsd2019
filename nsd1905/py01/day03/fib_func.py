def mk_fib():
    fib = [0, 1]
    n = int(input('长度: '))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = mk_fib()  # [0, 1, 1, 2, 3]
# print(a)
alist = [i * 2 for i in a]
print(alist)

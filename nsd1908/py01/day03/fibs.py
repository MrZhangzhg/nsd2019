def mk_fib():
    fib = [0, 1]

    n = int(input('长度: '))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

alist = mk_fib()
print(alist)
blist = [i * 2 for i in alist]
print(blist)

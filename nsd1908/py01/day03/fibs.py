def mk_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

for i in [5, 8, 6, 10, 20]:
    print(mk_fib(i))

# alist = mk_fib(5)
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)

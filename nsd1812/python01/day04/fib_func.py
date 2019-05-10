def gen_fib(n=10):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

alist = gen_fib()
print(alist)
print([i * 2 for i in alist])
print(gen_fib(5))

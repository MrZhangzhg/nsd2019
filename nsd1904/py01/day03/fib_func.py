def gen_fib():
    fib = [0, 1]

    n = int(input('数列长度: '))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

print(gen_fib())
nums = gen_fib()
alist = [i * 2 for i in nums]
print(alist)

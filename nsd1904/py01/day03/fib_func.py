def gen_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

print(gen_fib(5))
m = int(input('长度: '))
nums = gen_fib(m)
alist = [i * 2 for i in nums]
print(alist)

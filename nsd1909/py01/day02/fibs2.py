fib = [0, 1]

n = int(input('长度: '))

for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)

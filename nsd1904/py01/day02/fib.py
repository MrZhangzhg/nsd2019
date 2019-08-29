fib = [0, 1]

n = int(input('数列长度: '))

for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])  # 向列表中追加最后两项之和

print(fib)

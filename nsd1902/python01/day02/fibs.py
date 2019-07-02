fib = [0, 1]

for i in range(8):
    # 将列表中最后两项之和追加到列表尾部
    fib.append(fib[-1] + fib[-2])

print(fib)

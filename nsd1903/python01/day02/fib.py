# 特点：1.追加 2.追加的数字是列表中最后两个数之和
fib = [0, 1]

for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)

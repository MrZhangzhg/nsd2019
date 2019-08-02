def gen_fib():
    fib = [0, 1]

    n = int(input("长度: "))
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib   # 如果没有return，默认返回None

nums = gen_fib()
print(nums)
nums = [i * 2 for i in nums]
print(nums)

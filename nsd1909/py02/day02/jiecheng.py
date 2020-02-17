def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)
#              5 * func(4)  # 不能直接返回，需要将func(4)的结果与5相乘，得到的结果再返回
#              5 * 4 * func(3)
#              5 * 4 * 3 * func(2)
#              5 * 4 * 3 * 2 * func(1)
#              5 * 4 * 3 * 2 * 1

if __name__ == '__main__':
    print(func(5))

def func1(x):
    if x == 1:
        return 1
    else:
        return x * func1(x - 1)
    #          5 * func1(4)
    #          5 * 4 * func1(3)
    #          5 * 4 * 3 * func1(2)
    #          5 * 4 * 3 * 2 * func1(1)
    #          5 * 4 * 3 * 2 * 1

if __name__ == '__main__':
    print(func1(5))

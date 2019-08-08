def func1():
    print('in func1')
    func2()

# func1()  # 如果此调用func1将会报错，因为还不存在func2

def func2():
    print('in func2')

if __name__ == '__main__':
    func1()  # 可以正常调用，因为func2已经存在

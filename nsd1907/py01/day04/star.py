"""演示模块

这是一个用于演示的模块，它包含一个全局变量和一个函数
"""
hi = 'Hello World!'


def pstar(n=30):
    "用于打印n个星号"
    print('*' * n)


if __name__ == '__main__':
    print(hi)
    pstar()
    pstar(50)

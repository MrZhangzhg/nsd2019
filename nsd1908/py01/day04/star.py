"""演示模块

这是一个演示模块，它包含一个全局变量和一个函数
"""


hi = 'Hello World!'

def pstar(n=30):
    '默认打印30个星号，也可以指定个数'
    print('*' * n)

if __name__ == '__main__':
    print(hi)
    pstar(n=50)

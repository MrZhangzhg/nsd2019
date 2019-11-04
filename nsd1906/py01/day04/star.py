"""演示模块

该模块包含一个函数和一个全局变量
"""

hi = 'hello world!'

def pstar(n=30):
    "该函数用于打印星号，默认打印30个星号"
    print('*' * n)

if __name__ == '__main__':
    print(hi)
    pstar(40)

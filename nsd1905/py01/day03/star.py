'''打印星号

这是一个演示用的模块，只包含了一个全局变量和一个函数
'''

hi = 'Hello World'

def pstar(n=30):
    '缺省打印30个星号'
    print('*' * n)

if __name__ == '__main__':
    print(hi)
    pstar(40)

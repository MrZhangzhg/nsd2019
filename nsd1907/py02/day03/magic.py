class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # 打印实例时，执行此方法，必须返回字符串
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    pybook = Book('Python核心编程', '韦斯利')  # 调用__init__
    print(pybook)  # 调用__str__方法
    pybook()   # 调用__call__方法

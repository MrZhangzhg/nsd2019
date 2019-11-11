class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》是%s编写的' % (self.title, self.author))

if __name__ == '__main__':
    pybook = Book("Python基础教程", 'Magnus')  # 调用__init__
    print(pybook)  # 调用__str__
    pybook()  # 调用__call__

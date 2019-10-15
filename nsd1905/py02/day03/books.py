class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    # 实例化时自动调用__init__方法
    pybook = Book('python基础教程', 'Magnus Lie Hetland')
    print(pybook)  # 显示实例时，自动调用__str__方法
    pybook()  # 调用实例，自动调用__call__方法


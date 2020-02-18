class Book:
    def __init__(self, title, author):
        '创建实例时，自动调用的方法'
        self.title = title
        self.author = author

    def __str__(self):
        '在打印、显示实例时，自动调用'
        return '《%s》' % self.title

    def __call__(self):
        '使实例可以像函数一样调用'
        print('《%s》是%s编写的' % (self.title, self.author))

if __name__ == '__main__':
    py_book = Book('Python基础教程(第3版)', 'Magnus Lie Hetland')  # 调用__init__
    print(py_book)  # 调用__str__方法
    py_book()       # 调用__call__方法

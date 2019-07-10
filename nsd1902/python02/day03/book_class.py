class Book:
    def __init__(self, title, author):
        '实例化时自动调用'
        self.title = title
        self.author = author

    def __str__(self):
        '显示实例时自动调用'
        return "《%s》" % self.title

    def __call__(self):
        '实例调用时运行'
        print('《%s》是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('python核心编程', '韦斯利')  # 调用__init__
    print(core_py)   # 调用__str__
    core_py()    # 调用__call__


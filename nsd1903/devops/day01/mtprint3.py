import threading

class MyClass:
    def __call__(self):
        print('Hello World')

if __name__ == '__main__':
    a = MyClass()
    for i in range(3):
        t = threading.Thread(target=MyClass())  # target是MyClass的实例
        t.start()  # target()

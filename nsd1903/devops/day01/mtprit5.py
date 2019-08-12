import threading

class MyClass:
    def __init__(self, a):
        self.a = a

    def __call__(self, b, c):
        print('Hello', self.a, b, c)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=MyClass(10), args=(20, 30))
        t.start()  # target(*args)

import threading

class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self):
        print('Hello', self.a, self.b, self.c)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=MyClass(10, 20, 30))
        t.start()  # target(*args)

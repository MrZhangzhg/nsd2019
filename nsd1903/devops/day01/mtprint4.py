import threading

class MyClass:
    def __call__(self, a, b, c):
        print('Hello', a, b, c)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=MyClass(), args=(10, 20, 30))
        t.start()  # target(*args)

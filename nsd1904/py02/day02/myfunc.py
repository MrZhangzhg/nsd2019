def func1():
    print('Hello from func1')
    func2()

# func1()

def func2():
    print('Hello from func2')

if __name__ == '__main__':
    func1()

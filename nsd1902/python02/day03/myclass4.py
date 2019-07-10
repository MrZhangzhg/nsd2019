class A:
    def func1(self):
        print('A func')

    def func3(self):
        print('A func3')

class B:
    def func2(self):
        print('B func')

    def func3(self):
        print('B func3')

class C(B, A):
    def func3(self):
        print('C func3')

if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
    c1.func3()

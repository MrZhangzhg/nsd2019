class A:
    def func1(self):
        print('a func')

    def func4(self):
        print('***a func***')

class B:
    def func2(self):
        print('b func')

    def func4(self):
        print('###func b###')

class C(B, A):
    def func3(self):
        print('c func')

    def func4(self):
        print('^^^c func^^^')

if __name__ == '__main__':
    c1 = C()
    c1.func1()
    c1.func2()
    c1.func3()
    c1.func4()

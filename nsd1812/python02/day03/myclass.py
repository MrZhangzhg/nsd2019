class A:
    def foo(self):
        print('a foo')

    def fn1(self):
        print('a fn')

class B:
    def bar(self):
        print('b bar')

    def fn1(self):
        print('b fn')

class C(B, A):
    pass
    # def fn1(self):
    #     print('c fn')

if __name__ == '__main__':
    c1 = C()
    c1.foo()
    c1.bar()
    c1.fn1()

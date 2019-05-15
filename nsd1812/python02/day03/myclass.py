class A:
    def foo(self):
        print('a foo')

class B:
    def bar(self):
        print('b bar')

class C(A, B):
    pass

if __name__ == '__main__':
    c1 = C()
    c1.foo()
    c1.bar()

class A:
    def funca(self):
        print('class a')

    def func1(self):
        print('aaaaaaaaaaaaaaa')

class B:
    def funcb(self):
        print('class b')

    def func1(self):
        print('bbbbbbbbbbbbbbbb')

class C(B, A):
    def funcc(self):
        print('class c')

    # def func1(self):
    #     print('ccccccccccccc')

if __name__ == '__main__':
    c1 = C()
    c1.funca()
    c1.funcb()
    c1.funcc()
    c1.func1()

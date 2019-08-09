class A:
    def funca(self):
        print('A func')

    def funcd(self):
        print('in A')

class B:
    def funcb(self):
        print('B func')

    def funcd(self):
        print('In B')

class C(B, A):
    def funcc(self):
        print('C func')

if __name__ == '__main__':
    c1 = C()
    c1.funca()
    c1.funcb()
    c1.funcc()
    c1.funcd()


class A:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class C(A):
    def __init__(self, a, b, c, d, e):
        # A.__init__(self, a, b, c, d)
        super(C, self).__init__(a, b, c, d)
        self.e = e

if __name__ == '__main__':
    c1 = C(10, 20, 30, 40, 5)
    print(c1.a, c1.e)


class A:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class B(A):
    def __init__(self, a, b, c, d, e):
        # A.__init__(self, a, b, c, d)
        super(B, self).__init__(a, b, c, d)
        self.e = e

if __name__ == '__main__':
    b1 = B(10, 20, 30, 40, 50)
    print(b1.a, b1.e)

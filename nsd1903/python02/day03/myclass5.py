class A:
    def __init__(self, a, b, c, d, e, f, g):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

class B(A):
    def __init__(self, a, b, c, d, e, f, g, h):
        A.__init__(self, a, b, c, d, e, f, g)
        self.h = h

if __name__ == '__main__':
    b1 = B(1, 2, 3, 4, 5, 6, 7, 8)
class A:
    def func1(self):
        print('in A func1')

    def func4(self):
        print('A func4')

class B:
    def func2(self):
        print('in B func2')

    def func4(self):
        print('B func4')

class C(B, A):  # 父类可以有多个
    def func3(self):
        print('in C func3')

    def func4(self):
        print('C func4')

if __name__ == '__main__':
    c1 = C()    # 子类实例拥有所有类的方法
    c1.func1()
    c1.func2()
    c1.func3()
    c1.func4()




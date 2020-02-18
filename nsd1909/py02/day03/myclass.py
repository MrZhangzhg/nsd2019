class A:
    def func1(self):
        print('in A func1')

class B:
    def func2(self):
        print('in B func2')

class C(A, B):  # 父类可以有多个
    def func3(self):
        print('in C func3')

if __name__ == '__main__':
    c1 = C()    # 子类实例拥有所有类的方法
    c1.func1()
    c1.func2()
    c1.func3()




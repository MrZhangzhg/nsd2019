class Role:
    def __init__(self, name, wuqi, guojia):
        '称作构造器方法，创建实例时，自动调用。通常用于将属性绑定到实例。'
        self.name = name
        self.wuqi = wuqi
        self.guojia = guojia

    def show_me(self):
        # 绑定在实例身上的属性，可以在类中的任意位置使用
        print('我是%s，擅长使用%s' % (self.name, self.wuqi))

    def speak(self, words):
        # 没有绑定到实例的属性，就是函数的局部变量，只能在函数内使用
        print(words)

class ZhanShi(Role):  # 括号中是父类，也叫基类
    # 子类将会继承父类的所有方法
    def __init__(self, name, wuqi, guojia, zuoji):
        # Role.__init__(self, name, wuqi, guojia)  # 调用父类方法
        super(ZhanShi, self).__init__(name, wuqi, guojia)  # 调用父类方法，与上一行一样
        self.zuoji = zuoji

    def attack(self, target):
        print('正在近身与%s肉搏' % target)

class FaShi(Role):
    def attack(self, target):
        print('远程打击%s' % target)

if __name__ == '__main__':
    lb = ZhanShi('吕布', '方天画戟', '汉', '赤兔马')
    # lb.show_me()
    # lb.speak('马中赤兔，人中吕布')
    # lb.attack('张飞')
    # km = FaShi('孔明', '羽扇')
    # km.show_me()
    # km.speak('三分天下有其一')
    # km.attack('司马懿')

class Role:
    def __init__(self, name, wuqi):
        '称作构造器方法，创建实例时，自动调用。通常用于将属性绑定到实例。'
        self.name = name
        self.wuqi = wuqi

    def show_me(self):
        # 绑定在实例身上的属性，可以在类中的任意位置使用
        print('我是%s，擅长使用%s' % (self.name, self.wuqi))

    def speak(self, words):
        # 没有绑定到实例的属性，就是函数的局部变量，只能在函数内使用
        print(words)

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')  # 自动调用__init__方法
    lb.show_me()  # 实例lb自动作为第一个参数传给方法
    lb.speak('马中赤兔，人中吕布')
    zf = Role('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('我乃燕人张飞张冀德')

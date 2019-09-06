class GameRole:
    def __init__(self, nm, wp):
        "构造器方法，实例化时自动调用"
        self.name = nm
        self.weapon = wp

    def show_me(self):
        # 绑定到实例身上的属性，在各个方法中都可以使用
        print('我是：%s，我用的武器是：%s' % (self.name, self.weapon))

    def speak(self, words):
        # 参数就是函数的局部变量，只在函数内部可用
        print(words)

if __name__ == '__main__':
    # 实例化，调用__init__，实例本身自动作为第一个参数
    lb = GameRole('吕布', '方天画戟')
    print(lb.name)
    print(lb.weapon)
    lb.show_me()
    lb.speak('人在塔在')

    zf = GameRole('张飞', '蛇矛')
    print(zf.name)
    print(zf.weapon)
    zf.show_me()
    zf.speak('燕人张飞张冀德')

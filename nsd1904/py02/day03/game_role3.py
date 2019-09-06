class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是：%s，我用的武器是：%s' % (self.name, self.weapon))

class Warrior(GameRole):  # GameRole称作父类或基类
    "子类继承父类的所有方法"
    def __init__(self, nm, wp, gender):
        # self.name = nm
        # self.weapon = wp
        GameRole.__init__(self, nm, wp)
        self.gender = gender

    def attack(self, obj):
        print('正在攻击: %s' % obj)

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟', '男')
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.attack('董卓')

class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s, 我的武器是%s' % (self.name, self.weapon))

    def speak(self, content):
        print('%s在此, %s' % (self.name, content))

class Warrior(GameRole):  # GameRole称作父类或基类
    "子类可以继承父类的属性"
    def __init__(self, nm, weapon, gender):
        # GameRole.__init__(self, nm, weapon)
        super(Warrior, self).__init__(nm, weapon)  # 与上面一行等价
        self.gender = gender

    def attack(self):
        print('近身肉搏')

class Mage(GameRole):
    def attack(self):
        print('远程攻击')

if __name__ == '__main__':
    nz = Mage('哪吒', '火尖枪')
    hfh = Warrior('黄飞虎', '鞭', '男')
    print(hfh.gender)
    nz.show_me()
    hfh.show_me()
    nz.attack()
    hfh.attack()

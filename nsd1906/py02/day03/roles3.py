class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print('我是%s, %s' % (self.name, words))

    def attack(self, target):
        print('正在攻击: %s' % target)

class Warrior(Role):
    '子类可以继承父类(基类)的所有方法'
    def move(self):
        print('陆地移动')

class Mage(Role):
    pass

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    lj = Mage('李靖', '宝塔')
    lb.speak('马中赤兔，人中吕布')
    lj.speak('宝塔镇河妖')
    lb.move()

class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是: %s，擅用%s' % (self.name, self.weapon))

    def speak(self, word):
        # 没有绑定到实例身上的变量，就是函数的局部变量
        print(word)

class Warrior(Role):  # 括号中指定父类，父类也叫基类
    def attack(self, dst):
        print('攻击: %s' % dst)

class Mage(Role):
    pass

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    dc = Mage('貂蝉', '剑')
    lb.show_me()
    dc.show_me()
    lb.speak('人在塔在')
    lb.attack('董卓')

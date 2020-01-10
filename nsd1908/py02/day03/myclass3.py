class Role:
    def __init__(self, name, weapon):
        "__init__是构造器方法，创建实例时，它自动调用，一般用于将属性绑到对象"
        self.name = name
        self.weapon = weapon

    def show_me(self):
        "绑定在实例上的属性，在任意方法中都直接可用"
        print("我是%s, 我的兵器是%s" % (self.name, self.weapon))

    def say(self, words):
        "没有绑定的变量，是临时变量"
        print(words)

# 创建战士类，它的父类(也叫基类)是Role
class Warrior(Role):
    def __init__(self, name, weapon, country):
        # Role.__init__(self, name, weapon)
        # 以上调用父类方法的语句，也可以使用：
        super(Warrior, self).__init__(name, weapon)
        self.country = country

    def attack(self, target):
        print('近身攻击: %s' % target)

class Mage(Role):
    def attack(self, target):
        print('远程攻击: %s' % target)

if __name__ == '__main__':
    gy = Warrior('关羽', '青龙偃月刀', '蜀')
    km = Mage('孔明', '羽扇')
    gy.show_me()
    km.show_me()
    gy.attack('吕布')
    km.attack('周瑜')

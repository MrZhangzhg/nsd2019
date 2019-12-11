class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s, 我使用%s' % (self.name, self.weapon))

    def speak(self, words):
        print(words)

class Warrior(Role):  # 括号中是父类，也叫基类
    pass

class Mage(Role):
    def fly(self):
        print('I can fly.')

if __name__ == '__main__':
    # 实例化时，子类中没有__init__方法，将会寻找父类的相关方法
    lb = Warrior('吕布', '方天画戟')
    km = Mage('孔明', '扇子')
    lb.show_me()
    km.show_me()
    km.fly()
    # lb.fly()

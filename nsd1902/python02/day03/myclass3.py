class Role:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print("I'm %s, %s" % (self.name, words))

    def run(self):
        print('running...')

class Warrior(Role):
    def __init__(self, name, gender, weapon):
        # 以下两种写法都可以调用父类的方法，未加注释的是推荐写法
        # Role.__init__(self, name, weapon)
        super(Warrior, self).__init__(name, weapon)
        self.gender = gender

    def show_me(self):
        print("我是%s, 我是一个战士" % self.name)

if __name__ == '__main__':
    gy = Warrior('关羽', '男', '青龙偃月刀')
    gy.speak('过五关，斩六将')
    gy.show_me()

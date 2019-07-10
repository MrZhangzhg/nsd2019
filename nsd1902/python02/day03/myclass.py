class Warrior:
    def __init__(self, name, weapon):
        '实例化时自动调用'
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print("I'm %s, %s" % (self.name, words))

    def show_me(self):
        print("我是%s, 我是一个战士" % self.name)

if __name__ == '__main__':
    gy = Warrior('关羽', '青龙偃月刀')
    gy.speak('过五关，斩六将')
    gy.show_me()

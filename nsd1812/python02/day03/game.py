class GameCharacter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, word):
        print('我是%s, %s' % (self.name, word))

    def walk(self):
        print('我有%s，我能走' % self.weapon)


if __name__ == '__main__':
    lvbu = GameCharacter('吕布', '方天画戟')
    print(lvbu.name)
    print(lvbu.weapon)
    lvbu.speak('人在塔在')
    lvbu.walk()
    guanyu = GameCharacter('关羽', '青龙偃月刀')
    print(guanyu.name)
    print(guanyu.weapon)
    guanyu.speak('呵呵')

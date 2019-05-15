class Weapon:
    def __init__(self, wname, strength, type):
        self.name = wname
        self.strength = strength
        self.type = type

class GameCharacter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, word):
        print('我是%s, %s' % (self.name, word))

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100, '物理攻击')
    lvbu = GameCharacter('吕布', ji)
    print(lvbu.weapon.name)
    print(lvbu.weapon.type)

class GameCharacter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, word):
        print('我是%s, %s' % (self.name, word))

class Warrior(GameCharacter):  # 括号中指定父类(基类)
    def attack(self):
        print('近身肉搏')

class Mage(GameCharacter):
    def attack(self):
        print('远程攻击')

if __name__ == '__main__':
    gl = Warrior('盖伦', '大刀')
    tm = Mage('提莫', '蘑菇')
    gl.speak('人在塔在')
    gl.attack()
    tm.speak('我去前面用脸探探路')
    tm.attack()

class Weapon:
    def __init__(self, wname, strength):
        self.wname = wname
        self.strength = strength

class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print("I'm %s, %s" % (self.name, words))

    def show_me(self):
        print("我是%s, 我是一个战士。我用的武器是%s" % (self.name, self.weapon.wname))

if __name__ == '__main__':
    blade = Weapon('青龙偃月刀', 100)
    print(blade.wname, blade.strength)
    gy = Warrior('关羽', blade)
    gy.show_me()
    cz = Weapon('禅杖', 100)
    lzs = Warrior('鲁智深', cz)
    lzs.show_me()

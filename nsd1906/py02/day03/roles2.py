class Weapon:
    def __init__(self, name, strength, type):
        self.name = name
        self.strength = strength
        self.type = type

class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    ji = Weapon('方天画戟', '88', '物理伤害')
    # print(ji.name, ji.strength, ji.type)
    lb = Warrior('吕布', ji)
    print(lb.weapon.name, lb.weapon.type)



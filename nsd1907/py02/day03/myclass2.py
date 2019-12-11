class Weapon:
    def __init__(self, nm, strength):
        self.name = nm
        self.strength = strength

class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    wp = Weapon('方天画戟', 100)
    lb = Role('吕布', wp)
    print(wp.name, wp.strength)
    print(lb.weapon.name)
    print(lb.weapon.strength)

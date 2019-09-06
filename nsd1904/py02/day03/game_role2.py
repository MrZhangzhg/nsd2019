class Weapon:
    def __init__(self, wnm, strength):
        self.wname = wnm
        self.strength = strength

class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100)
    print(ji.wname)
    lb = GameRole('吕布', ji)

    print(lb.name)
    print(lb.weapon.wname)
    print(lb.weapon.strength)


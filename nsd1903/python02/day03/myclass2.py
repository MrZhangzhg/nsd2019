class Weapon:
    def __init__(self, nm, strength):
        self.wname = nm
        self.stength = strength

class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100)
    lb = GameRole('吕布', ji)
    print(lb.name)
    # print(ji.wname)
    print(lb.weapon.wname)

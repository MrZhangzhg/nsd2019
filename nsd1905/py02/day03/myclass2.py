class Weapon:
    def __init__(self, nm, type):
        self.wname = nm
        self.type = type

class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是: %s，擅用%s' % (self.name, self.weapon))

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理攻击')
    lb = Role('吕布', ji)
    print(ji.wname, ji.type)
    print(lb.weapon.wname, lb.weapon.type)

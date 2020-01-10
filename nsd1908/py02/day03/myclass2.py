class Weapon:
    def __init__(self, wname, wtype, strength):
        self.wname = wname
        self.wtype = wtype
        self.strength = strength

class Role:
    def __init__(self, name, weapon):
        "__init__是构造器方法，创建实例时，它自动调用，一般用于将属性绑到对象"
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    ji = Weapon('方天画戟', '物理', 100)
    lb = Role('吕布', ji)
    print(ji.wname, ji.wtype, ji.strength)
    print(lb.weapon.wname, lb.weapon.wtype, lb.weapon.strength)

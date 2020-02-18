class WuQi:
    def __init__(self, wname, wtype, liliang):
        self.wname = wname
        self.wtype = wtype
        self.liliang = liliang

class Role:
    def __init__(self, name, wuqi):
        '称作构造器方法，创建实例时，自动调用。通常用于将属性绑定到实例。'
        self.name = name
        self.wuqi = wuqi

    def show_me(self):
        # 绑定在实例身上的属性，可以在类中的任意位置使用
        print('我是%s，擅长使用%s' % (self.name, self.wuqi))


if __name__ == '__main__':
    ji = WuQi('方天画戟', wtype='物理伤害', liliang=100)
    print(ji.wname, ji.wtype, ji.liliang)
    lb = Role('吕布', ji)  # 自动调用__init__方法
    print(lb.wuqi.wname, lb.wuqi.wtype, lb.wuqi.liliang)

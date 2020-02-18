
class Role:
    def __init__(self, name, wuqi):
        '称作构造器方法，创建实例时，自动调用'
        self.name = name
        self.wuqi = wuqi

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')

class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法
    # 调用通过类创建的方法，实例自动作为第一个参数传递
    lb = GameRole('吕布', '方天画戟')  # 创建名为lb的实例
    print(lb.name, lb.weapon)

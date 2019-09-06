class GameRole:
    def __init__(self, nm, wp):
        "构造器方法，实例化时自动调用"
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    # 实例化，调用__init__，实例本身自动作为第一个参数
    lb = GameRole('吕布', '方天画戟')
    print(lb.name)
    print(lb.weapon)

    zf = GameRole('张飞', '蛇矛')
    print(zf.name)
    print(zf.weapon)

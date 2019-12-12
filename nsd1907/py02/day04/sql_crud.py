# create / retrieve / update / delete
from dbconn import Session, Departments, Employees

# 创建到数据库的会话连接
session = Session()

# 插入数据
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
sales = Departments(dep_id=5, dep_name='销售部')
market = Departments(dep_id=6, dep_name='市场部')
session.add_all([hr, ops, dev, qa, sales, market])


# 如果是增删改操作，需要确认commit
session.commit()

# 关闭会话
session.close()

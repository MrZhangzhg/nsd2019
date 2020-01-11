# create / retrieve / update / delete
from dbconn import Departments, Employees, Salary, Session

# 创建到数据库的会话实例
session = Session()

# 执行增删改查操作
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
market = Departments(dep_id=5, dep_name='市场部')
sales = Departments(dep_id=6, dep_name='销售部')
session.add_all([hr, ops, dev, qa, market, sales])

# 确认
session.commit()

# 关闭
session.close()

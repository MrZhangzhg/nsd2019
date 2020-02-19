from dbconn import Session, Department, Employee

# 创建到数据库的会话连接
session = Session()

# 执行增删改查
# 创建部门
hr = Department(dep_id=1, dep_name='人事部')
ops = Department(dep_id=2, dep_name='运维部')
dev = Department(dep_id=3, dep_name='开发部')
qa = Department(dep_id=4, dep_name='测试部')
finance = Department(dep_id=5, dep_name='财务部')
market = Department(dep_id=6, dep_name='市场部')
session.add_all([hr, ops, dev, qa, finance, market])

# 确认
session.commit()

# 关闭会话连接
session.close()

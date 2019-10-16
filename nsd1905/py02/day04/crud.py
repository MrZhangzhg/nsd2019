from dbconn import Session, Departments, Employees

# 创建到数据库的会话连接
session = Session()

# 对数据库进行增删改查操作
#######################################
# 增加部门
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
market = Departments(dep_id=5, dep_name='市场部')
sales = Departments(dep_id=6, dep_name='销售部')
session.add_all([hr, ops, dev, qa, market, sales])
# 创建员工记录
lb = Employees(
    emp_id=1, emp_name='刘备',
    birth_date='1970-1-1', email='lb@tedu.cn', dep_id=1
)
gy = Employees(
    emp_id=2, emp_name='关羽',
    birth_date='1973-5-4', email='gy@qq.com', dep_id=2
)
zf = Employees(
    emp_id=3, emp_name='张飞',
    birth_date='1974-10-1', email='zf@tedu.cn', dep_id=2
)
zy = Employees(
    emp_id=4, emp_name='赵云',
    birth_date='1976-8-1', email='zy@qq.com', dep_id=3
)
session.add_all([lb, gy, zf, zy])

# 如果对数据库有改动，需要确认
session.commit()

# 关闭会话
session.close()

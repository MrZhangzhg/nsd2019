from dbconn import Departments, Employees, Salary, Session

# 创建会话实例，用于连接数据库
session = Session()

# 创建员工实例
mxz = Employees(
    emp_id=1,
    emp_name='孟宪峥',
    birth_date='1994-05-28',
    email='mxz@163.com',
    dep_id=2
)
wj = Employees(
    emp_id=2,
    emp_name='翁俊',
    birth_date='1996-03-21',
    email='wj@qq.com',
    dep_id=2
)
xzc = Employees(
    emp_id=3,
    emp_name='向子辰',
    birth_date='1995-08-09',
    email='xzc@qq.com',
    dep_id=3
)
llc = Employees(
    emp_id=4,
    emp_name='李良辰',
    birth_date='1995-12-20',
    email='llc@tedu.cn',
    dep_id=2
)
yty = Employees(
    emp_id=5,
    emp_name='岳天宇',
    birth_date='1992-01-15',
    email='yty@163.com',
    dep_id=3
)
wxm = Employees(
    emp_id=6,
    emp_name='王续敏',
    birth_date='1995-02-18',
    email='wxm@qq.com',
    dep_id=1
)
lt = Employees(
    emp_id=7,
    emp_name='刘涛',
    birth_date='1997-08-19',
    email='lt@tedu.cn',
    dep_id=3
)
wy = Employees(
    emp_id=8,
    emp_name='汪洋',
    birth_date='1996-11-08',
    email='wy@163.com',
    dep_id=2
)
mzy = Employees(
    emp_id=9,
    emp_name='莫振宇',
    birth_date='1994-06-10',
    email='mzy@qq.com',
    dep_id=4
)


# 在数据库中创建记录
emps = [mxz, wj, xzc, llc, yty, wxm, lt, wy, mzy]
session.add_all(emps)
session.commit()   # 确认至数据库

# 关闭会话
session.close()

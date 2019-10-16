from dbconn import Session, Departments, Employees

# 创建到数据库的会话连接
session = Session()

# 对数据库进行增删改查操作
#######################################
# 增加部门
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# market = Departments(dep_id=5, dep_name='市场部')
# sales = Departments(dep_id=6, dep_name='销售部')
# session.add_all([hr, ops, dev, qa, market, sales])
#######################################
# 创建员工记录
# lb = Employees(
#     emp_id=1, emp_name='刘备',
#     birth_date='1970-1-1', email='lb@tedu.cn', dep_id=1
# )
# gy = Employees(
#     emp_id=2, emp_name='关羽',
#     birth_date='1973-5-4', email='gy@qq.com', dep_id=2
# )
# zf = Employees(
#     emp_id=3, emp_name='张飞',
#     birth_date='1974-10-1', email='zf@tedu.cn', dep_id=2
# )
# zy = Employees(
#     emp_id=4, emp_name='赵云',
#     birth_date='1976-8-1', email='zy@qq.com', dep_id=3
# )
# session.add_all([lb, gy, zf, zy])
#######################################
# 查询，查询的参数是类，返回的是实例列表
# qset1 = session.query(Departments)
# print(qset1)  # qset1只是一个sql语句，只有取值的时候才会真正查询
# print(qset1.all())  # all返回列表
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
#######################################
# 查询，查询的参数是类变量，返回的是由变量构成的元组列表
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2.all())
#######################################
# 排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
#######################################
# 取切片
# qset4 = session.query(Departments).order_by(Departments.dep_id)[2:4]
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
#######################################
# 过滤
# qset5 = session.query(Departments).filter(Departments.dep_id>3)
# for dep in qset5:
#     print(dep.dep_id, dep.dep_name)
# 过滤的结果，还可以继续过滤
# qset6 = session.query(Departments).filter(Departments.dep_id>3)\
#     .filter(Departments.dep_id<6)
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name)
#######################################
# 查询tedu.cn作为结尾的邮箱
# qset7 = session.query(Employees).filter(Employees.email.like('%tedu.cn'))
# for emp in qset7:
#     print(emp.emp_name, emp.email)
#######################################
# 查询1、2号部门有哪些人
# qset8 = session.query(Employees).filter(Employees.dep_id.in_([1, 2]))
# for emp in qset8:
#     print(emp.emp_name, emp.dep_id)
#######################################
# 查询不在1、2号部门有哪些人
# qset9 = session.query(Employees).filter(~Employees.dep_id.in_([1, 2]))
# for emp in qset9:
#     print(emp.emp_name, emp.dep_id)
#######################################
# 多表查询。因为两张表有主外键约束关系，所以查询时，它们自动匹配
# query中先写Employees，join时就写Departments
# qset10 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments)
# for data in qset10:
#     print(data)
#######################################
# all返回满足条件的列表
# first返回all中的第一个结果
# qset11 = session.query(Departments)
# print(qset11.all())
# print('*' * 30)
# print(qset11.first())
# d1 = qset11.all()[0]
# print(d1.dep_name)
# d2 = qset11.first()
# print(d2.dep_name)
#######################################
# 修改
# qset12 = session.query(Departments).filter(Departments.dep_name=='人事部')
# hr = qset12.first()
# hr.dep_name = '人力资源部'
#######################################
# 删除
qset13 = session.query(Departments).filter(Departments.dep_id==6)
sales = qset13.first()
session.delete(sales)



# 如果对数据库有改动，需要确认
session.commit()

# 关闭会话
session.close()

from dbconn import Session, Department, Employee

# 创建到数据库的会话连接
session = Session()

# 执行增删改查
# 创建部门
# hr = Department(dep_id=1, dep_name='人事部')
# ops = Department(dep_id=2, dep_name='运维部')
# dev = Department(dep_id=3, dep_name='开发部')
# qa = Department(dep_id=4, dep_name='测试部')
# finance = Department(dep_id=5, dep_name='财务部')
# market = Department(dep_id=6, dep_name='市场部')
# session.add_all([hr, ops, dev, qa, finance, market])

# 创建员工
# xcw = Employee(
#     emp_id=1, emp_name='许陈碗',
#     email='xcw@tedu.cn', dep_id=1
# )
# lyx = Employee(
#     emp_id=2, emp_name='刘元新',
#     email='lyx@tedu.cn', dep_id=2
# )
# sw = Employee(
#     emp_id=3, emp_name='沈炜',
#     email='sw@qq.com', dep_id=2
# )
# zl = Employee(
#     emp_id=4, emp_name='钟力',
#     email='zl@163.com', dep_id=3
# )
# hn = Employee(
#     emp_id=5, emp_name='浩宁',
#     email='hn@163.com', dep_id=4
# )
# session.add_all([xcw, lyx, sw, zl, hn,])

# 基础查询1：将类作为参数，返回实例构成的列表
qset1 = session.query(Department)
# print(qset1)  # 只是一个SQL语句，当向它取值时，sql语句才执行
# for bumen in qset1:
#     print(bumen.dep_id, bumen.dep_name)

# 基础查询2：将类变量作为参数，返回的是各个属性构成的元组，元组构成列表
qset2 = session.query(Employee.emp_name, Employee.email)
# for data in qset2:
#     print(data)



# 可以对查询的结果进一步应用其他方法
qset3 = session.query(Department).order_by(Department.dep_id)
# for bumen in qset3:
#     print(bumen.dep_id, bumen.dep_name)

# get方法，可以根据主键取出实例
# dep = session.query(Department).get(1)
# print(type(dep))
# print(dep.dep_id, dep.dep_name)

# filter方法，实现sql语句中的where，它返回的是列表，列表长度是0到多
qset4 = session.query(Department).filter(Department.dep_id>2).order_by(Department.dep_id)
# for bumen in qset4:
#     print(bumen.dep_id, bumen.dep_name)

# filter方法，可以多次使用
qset5 = session.query(Department).filter(Department.dep_id>2).filter(Department.dep_id<5)
for bumen in qset5:
    print(bumen.dep_id, bumen.dep_name)



# 修改，将人事部改为人力资源部
# qset3 = session.query(Department).filter(Department.dep_id==1)
# hr = qset3.first()
# hr.dep_name = '人力资源部'


# 删除，删除市场部
# qset4 = session.query(Department).filter(Department.dep_id==6)
# market = qset4.first()
# session.delete(market)

# 确认
session.commit()

# 关闭会话连接
session.close()

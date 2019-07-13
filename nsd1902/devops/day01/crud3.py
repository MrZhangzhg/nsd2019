from dbconn import Session, Departments, Employees

# 1. 创建一个会话实例
session = Session()

#################################
# 查询数据库，返回实体类的实例
# qset1 = session.query(Departments)
# print(qset1)  # 此时只是一条SQL语句，不真正连接数据库
# print(list(qset1))  # 取值的时候，才会连接数据库
# for dep in qset1:
#     print('部门ID: %s, 部门名称: %s' % (dep.dep_id, dep.dep_name))
#################################
# 如果查询某些字段，返回的是元组
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2)   # qset2是SQL语句
# print(list(qset2))   # 取值是元组
#################################
# 排序，可以对执行结果进一步操作
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
#################################
# 排序，取切片
# qset4 = session.query(Departments).order_by(Departments.dep_id)[2:4]
# print(qset4)  # 因为qset4执行了切片取值，所以它不是sql语句了
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
#################################
# 过滤，查找2号部门的员工
qset5 = session.query(Employees).filter(Employees.dep_id==2)
for emp in qset5:
    print(emp.emp_name)






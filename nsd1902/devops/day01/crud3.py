from dbconn import Session, Departments, Employees

# 1. 创建一个会话实例
session = Session()

#################################
# 查询数据库，返回实体类的实例
qset1 = session.query(Departments)
print(qset1)  # 此时只是一条SQL语句，不真正连接数据库
print(list(qset1))  # 取值的时候，才会连接数据库
for dep in qset1:
    print('部门ID: %s, 部门名称: %s' % (dep.dep_id, dep.dep_name))



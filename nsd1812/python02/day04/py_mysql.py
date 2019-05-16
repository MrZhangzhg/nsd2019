import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1812',
    charset='utf8'
)

cursor = conn.cursor()

#############################################
# 创建表
# create_dep = '''CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(50),
# PRIMARY KEY(dep_id)
# )'''
# create_emp = '''CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(50), email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )'''
# create_sal = '''CREATE TABLE salary(
# id INT, date DATE, emp_id INT, basic INT, awards INT,
# PRIMARY KEY(id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )'''
#
# cursor.execute(create_dep)
# cursor.execute(create_emp)
# cursor.execute(create_sal)
#############################################
# 插入语句
# insert_dep = 'INSERT INTO departments VALUES(%s, %s)'
# cursor.executemany(insert_dep, [(1, '人事部')])
# deps = [(2, '财务部'), (3, '运维部'), (4, '开发部'), (5, '测试部'), (6, '市场部')]
# cursor.executemany(insert_dep, deps)
#############################################
# 基础查询
# select1 = 'SELECT * FROM departments'
# cursor.execute(select1)
# print(cursor.fetchone())
# print('*' * 20)
# print(cursor.fetchmany(2))
# print('*' * 20)
# print(cursor.fetchall())
#############################################
# 移动游标
# select1 = 'SELECT * FROM departments ORDER BY dep_id'
# cursor.execute(select1)
# cursor.scroll(2, mode='relative')  # 以相对方式向下移动2行记录
# print(cursor.fetchone())
# print('*' * 20)
# cursor.scroll(0, mode='absolute')  # 以绝对方式移动到第1行记录
# print(cursor.fetchone())
#############################################
# 修改
# update1 = 'UPDATE departments set dep_name=%s WHERE dep_name=%s'
# cursor.execute(update1, ('人力资源部', '人事部'))
#############################################
# 删除
delete1 = 'DELETE FROM departments WHERE dep_name=%s'
cursor.execute(delete1, ('市场部',))




conn.commit()

cursor.close()
conn.close()

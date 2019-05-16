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
insert_dep = 'INSERT INTO departments VALUES(%s, %s)'
cursor.executemany(insert_dep, [(1, '人事部')])
deps = [(2, '财务部'), (3, '运维部'), (4, '开发部')]
cursor.executemany(insert_dep, deps)
#############################################



conn.commit()

cursor.close()
conn.close()

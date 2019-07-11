import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1902',
    charset='utf8'
)

# 创建游标，用于将来执行SQL语句
cursor = conn.cursor()

# 编写需要执行的SQL语句
create_dep = '''CREATE TABLE departments(
dep_id INT,
dep_name VARCHAR(20),
PRIMARY KEY(dep_id)
)'''
create_emp = '''CREATE TABLE employees(
emp_id INT,
emp_name VARCHAR(20),
birth_date DATE,
phone VARCHAR(11),
email VARCHAR(50),
dep_id INT,
PRIMARY KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)'''
create_sal = '''CREATE TABLE salary(
id INT,
date DATE,
emp_id INT,
basic INT,
awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''

# 执行SQL语句
cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)

# 确认
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()

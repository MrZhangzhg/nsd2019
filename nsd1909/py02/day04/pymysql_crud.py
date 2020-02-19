# crud: create增/retrieve查/update改/delete删
import pymysql

# 建立连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='root', passwd='tedu.cn',
    db='nsd1909', charset='utf8'
)

# 创建游标。游标类似于文件对象，通过文件对象可以对文件读写，通过游标对数据库进行操作
cur = conn.cursor()

# 编写并执行相应的sql语句
# 添加部门的语句
sql1 = 'INSERT INTO departments VALUES (%s, %s)'
# 添加1个部门
# cur.execute(sql1, (1, '人事部'))
# 添加多个部门
# cur.executemany(sql1, [(2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '财务部'), (6, '市场部')])

# 查询
sql2 = 'SELECT * FROM departments ORDER BY dep_id'
# cur.execute(sql2)
# result1 = cur.fetchone()    # 取出一条记录
# print(result1)
# print('*' * 50)
# result2 = cur.fetchmany(2)  # 继续向后取出2条记录
# print(result2)
# print('*' * 50)
# result3 = cur.fetchall()    # 继续向后取出全部记录
# print(result3)

# 修改
sql3 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# cur.execute(sql3, ('人力资源部', '人事部'))

# 删除
sql4 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(sql4, (6,))  # 即使只有一项内容，第2个参数也必须是元组

# 确认
conn.commit()

# 关闭游标、关闭连接
cur.close()
conn.close()





import pymysql

# 创建到数据库服务器的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1905',
    charset='utf8'
)

# 创建游标
cur = conn.cursor()

# 执行sql语句
# 创建部门
# insert1 = 'INSERT INTO departments VALUES(%s, %s)'
# hr = [(1, '人事部')]
# deps = [(2, 'ops'), (3, 'dev'), (4, 'qa'), (5, 'market'), (6, 'sales')]
# cur.executemany(insert1, hr)
# cur.executemany(insert1, deps)
############################################
# 查询
# select1 = 'SELECT * FROM departments'
# cur.execute(select1)
# result1 = cur.fetchone()  # 取一个记录
# print(result1)
# result2 = cur.fetchmany(2)   # 继续取2个记录
# print(result2)
# result3 = cur.fetchall()   # 继续取剩余全部记录
# print(result3)
############################################
# 移动游标
# select1 = 'SELECT * FROM departments'
# cur.execute(select1)
# cur.scroll(2, mode='absolute')  # absolute总是从开头算起
# result1 = cur.fetchone()
# print(result1)
# cur.scroll(1)  # 默认以相对方式移动，即从当前位置移动
# result2 = cur.fetchone()
# print(result2)
############################################
# 修改
update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cur.execute(update1, ('人力资源部', '人事部'))
############################################
# 删除
delete1 = 'DELETE FROM departments WHERE dep_id=%s'
cur.execute(delete1, (6,))

# 对数据库有改动，需要确认
conn.commit()

# 关闭
cur.close()
conn.close()

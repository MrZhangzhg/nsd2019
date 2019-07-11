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

# 查询
query_dep = 'SELECT * FROM departments'
cursor.execute(query_dep)
result1 = cursor.fetchone()  # 取一行
print(result1)
print('*' * 40)
result2 = cursor.fetchmany(2)  # 指定取出几行
print(result2)
print('*' * 40)
result3 = cursor.fetchall()   # 取出全部
print(result3)

# 关闭游标和连接
cursor.close()
conn.close()

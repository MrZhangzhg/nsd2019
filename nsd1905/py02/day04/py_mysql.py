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

# 编写sql语句


# 执行sql语句

# 关闭
cur.close()
conn.close()

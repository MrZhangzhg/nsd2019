import pymysql

# 创建到数据库服务器的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1906',
    charset='utf8'
)

# 创建游标。游标就像是文件对象，通过文件对象可以对文件读写
# 通过游标，可以对数据实现增删改查
cur = conn.cursor()

# 编写sql语句
insert1 = 'INSERT INTO departments VALUES(%s, %s)'

# 执行sql语句
hr = (1, '人事部')
ops = (2, '运维部')
dev = (3, '开发部')
qa = (4, '测试部')
sales = (5, '销售部')
market = (6, '市场部')

cur.executemany(insert1, [hr])
cur.executemany(insert1, [ops, dev, qa, sales, market])

# 如果是增删改操作，需要commit
conn.commit()

# 关闭
cur.close()
conn.close()

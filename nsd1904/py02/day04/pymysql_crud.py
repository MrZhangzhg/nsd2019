import pymysql

# 创建到数据的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1904',
    charset='utf8'
)

cur = conn.cursor()  # 创建游标，相当于文件对象
###################################


###################################
conn.commit()
cur.close()
conn.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建引擎，用于指定操作的数据库
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?选项
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1909?charset=utf8',
    encoding='utf8',  # 字符编码
    echo=True         # 在终端上打印debug日志信息，生产环境下不要打开
)

# 创建会话类，用于连接到数据库，通过会话连接操作数据库
Session = sessionmaker(bind=engine)

# 创建实体类(数据库中表对应的类)的基类
Base = declarative_base()


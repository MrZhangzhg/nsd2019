from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 创建到数据库的连接引擎

engine = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1906?charset=utf8',
    encoding='utf8',
    # echo=True  # 在终端显示debug日志，生产环境勿用
)
# 创建基类
Base = declarative_base()

# 创建实体类，必须继承基类
class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

if __name__ == '__main__':
    # 如果库中不存在对应的表则创建；存在就不创建了
    Base.metadata.create_all(engine)



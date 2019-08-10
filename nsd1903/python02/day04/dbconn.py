from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 创建到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1903?charset=utf8',
    encoding='utf8',
    echo=True  # 打印日志信息，生产环境下不要启用
)

# 创建实体类的基类
Base = declarative_base()

# 创建实体类
class Departments(Base):
    __tablename__ = 'departments'  # 设置与库中的哪张表关联
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

if __name__ == '__main__':
    # 库中无表则创建，有表不会再创建
    Base.metadata.create_all(engine)

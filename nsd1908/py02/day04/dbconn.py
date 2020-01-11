from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 创建连接到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1908?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出日志
)

# 创建实体类（与表关联的类）的基类
Base = declarative_base()

# 创建实体类
class Departments(Base):
    __tablename__ = 'departments'  # 定义库中关联的表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

if __name__ == '__main__':
    # 如果库中没有相关的表则创建，如果已存在，只是映射，不会再创建一遍
    Base.metadata.create_all(engine)

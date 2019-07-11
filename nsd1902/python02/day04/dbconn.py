from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?字符集参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1902?charset=utf8',
    # 编码方案
    encoding='utf8',
    # echo=True   # 打开调试模式，生产环境不要设置
)

# 创建一个会话类，只有在CRUD，即增删改查时需要，本模块文件实际上用不到
# 为了在其他模块文件中可以直接调用，在本模块中创建
Session = sessionmaker(bind=engine)

# 生成实体类的基类
Base = declarative_base()

# 创建部门表的实体类，类名自定义，必须继承自Base
class Departments(Base):
    __tablename__ = 'departments'  # 此类关联departments表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

# 创建员工表的实体类
class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    # dep_id与departments的dep_id构成外键约束关系
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

# 创建工资表的实体类
class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 库中无表则创建，有表只是关联，不会再覆盖
    Base.metadata.create_all(engine)

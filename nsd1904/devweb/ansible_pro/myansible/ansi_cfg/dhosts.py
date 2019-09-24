#!/root/nsd1904/bin/python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engin = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1904/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engin)

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ipaddr = Column(String(15))
    group_id = Column(ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    result = {}
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    for group, ip in qset:
        if group not in result:
            result[group] = {}  # {'dbservers': {}}
            result[group]['hosts'] = []  # {'dbservers': {'hosts': []}}
        result[group]['hosts'].append(ip)
    print(json.dumps(result))   # 输出要求是json格式，而不是字典

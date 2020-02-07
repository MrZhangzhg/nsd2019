#!/root/nsd1908/bin/python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1908/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100))
    ipaddr = Column(String(15))
    group_id = Column(ForeignKey('webadmin_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Host.ipaddr, HostGroup.groupname).join(HostGroup)
    # print(qset.all())
    result = {}
    for ip, group in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(result)

#!/root/nsd1902/bin/python
import json
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1902/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webadmin_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(100), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_hostgroup.id'))


if __name__ == '__main__':
    result = {}
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    # [('dbservers', '192.168.4.5'), ('webservers', '192.168.4.6'), ('webservers', '192.168.4.7')]
    for group, ip in qset:
        if group not in result:
            result[group] = {}
        if not result[group]:
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(json.dumps(result))

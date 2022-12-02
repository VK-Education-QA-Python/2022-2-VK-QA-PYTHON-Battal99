from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=16))
    password = Column(String(length=255))
    email = Column(String(length=64))
    access = Column(SmallInteger, default=1)
    active = Column(SmallInteger, default=0)
    start_active_time = Column(DateTime, nullable=True)

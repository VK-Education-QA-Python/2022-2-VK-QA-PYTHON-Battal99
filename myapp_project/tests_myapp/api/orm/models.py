from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)
    username = Column(String(length=16),  nullable=False)
    surname = Column(String(length=16),  nullable=True)
    password = Column(String(length=255),  nullable=False)
    email = Column(String(length=64),  nullable=False)
    access = Column(SmallInteger, default=1)
    active = Column(SmallInteger, default=0)
    start_active_time = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'name={self.name}, username={self.username}'

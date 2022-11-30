from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR
from utils.constant import TablesName


Base = declarative_base()


class BadRequests(Base):
    """ Запросы с ошибкой 4xx """
    __tablename__ = TablesName.BadRequests.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(300), nullable=False)
    status_code = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    ip_address = Column(VARCHAR(100), nullable=False)

    def __repr__(self):
        return f"BadRequests:(id={self.id}, " \
               f"url={self.ip_address}, " \
               f"count={self.count})" \
               f"status_code={self.status_code}," \
               f"ip_address={self.ip_address}"


class TopRequests(Base):
    """ Общее количество запросов """
    __tablename__ = TablesName.TopRequests.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_method = Column(VARCHAR(300), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"TopRequests:(id={self.id}, " \
               f"name_method={self.name_method}, " \
               f"count={self.count})"


class ServerErrorIp(Base):
    """ пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой """
    __tablename__ = TablesName.ServerErrorIp.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(VARCHAR(100), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"ServerErrorIp:(id={self.id}, " \
               f"ip_address={self.ip_address}, " \
               f"count={self.count})"


class UrlRequests(Base):
    """ Количество url"""
    __tablename__ = TablesName.UrlRequests.value

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(100), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"UrlRequests:(id={self.id}, " \
               f"url={self.url}, " \
               f"count={self.count})"

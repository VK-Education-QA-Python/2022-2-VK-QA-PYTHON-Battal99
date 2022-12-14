import sqlalchemy
import allure
from sqlalchemy.orm import sessionmaker

from orm.models import User


class MySqlClient:

    def __init__(self, db_name, user, password, host='127.0.0.1', port='3306'):
        self.password = password
        self.user = user
        self.port = port
        self.db_name = db_name
        self.host = host

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)  # session creation wrapper
        self.session = session()

    def truncate_table(self):
        self.connect()
        self.session.query(User).delete()
        self.session.commit()
        self.connection.close()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    @allure.step("find person db")
    def find_person(self, username):
        result = str(
            self.session.query(User).filter_by(username=username).one()
        )
        if result:
            return result
        allure.attach(str(result), 'result', allure.attachment_type.TEXT)
        return None

    @allure.step("access user db")
    def get_access_user(self, user):
        """ Получаем из БД значение атрибута access пользователя """
        access = self.session.query(
            User.access
        ).filter(User.username == user.username).one()[0]
        allure.attach(str(access), 'access', allure.attachment_type.TEXT)
        return access

    @allure.step("count users db")
    def count_user(self):
        """ Количество пользователей"""
        count = self.session.query(User).count()
        allure.attach(str(count), 'count', allure.attachment_type.TEXT)
        return count

    @allure.step("check active user (0 - inactive, 1 - active")
    def check_active_user(self, username):
        """ Проверка атрибута active у пользователя"""
        active = self.session.query(
            User.active
        ).filter(User.username == username).one()[0]
        allure.attach(str(active), 'access', allure.attachment_type.TEXT)
        return active

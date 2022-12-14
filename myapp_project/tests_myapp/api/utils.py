import allure
from faker import Faker

from orm.client_orm import MySqlClient
# from settings import DB_NAME, DB_USER, DB_PASSWORD
from settings import DB_NAME, DB_USER, DB_PASSWORD


class FakeUser:

    fake = Faker()
    username = None
    name = None
    surname = None
    password = None
    email = None

    @allure.step('Init user')
    def __init__(self):
        username = FakeUser.fake.unique.first_name()
        min_length_name = 8
        while len(username) < min_length_name:
            username = FakeUser.fake.unique.first_name()
        self.username = username
        self.name = FakeUser.fake.unique.first_name()
        self.password = ''.join(FakeUser.fake.words(3))
        self.email = FakeUser.fake.unique.last_name() + '@mail.ru'
        self.surname = FakeUser.fake.unique.first_name()
        self.allure_display()

    def allure_display(self):
        record = f"Name: {self.username} \
        \nEmail: {self.email} \
        \nPassword: {self.password}"
        allure.attach(record, 'User', allure.attachment_type.TEXT)


def mysql_client():
    client = MySqlClient(db_name=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    client.connect(db_created=True)
    return client

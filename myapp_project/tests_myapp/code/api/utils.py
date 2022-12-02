from faker import Faker
import allure


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
        min_length_name = 7
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

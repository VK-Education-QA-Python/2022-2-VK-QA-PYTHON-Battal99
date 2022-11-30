import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.model import Base
from utils.constant import TablesName


class SqlClient:

    def __init__(self, db_name, user, password):
        self.user = user
        self.port = '3306'
        self.password = password
        self.host = '127.0.0.1'
        self.db_name = db_name

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}' \
              f'@{self.host}:{self.port}/{db}'
        self.engine = sqlalchemy.create_engine(url)
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        try:
            self.connect(db_created=False)
            self.execute_query(f'DROP database if exists {self.db_name}',
                               fetch=False)
            self.execute_query(f'CREATE database {self.db_name}',
                               fetch=False)
        finally:
            self.connection.close()

    def create_tables(self):
        for table in TablesName:
            if not sqlalchemy.inspect(self.engine).has_table(table.value):
                Base.metadata.tables[table.value].create(self.engine)

    def execute_query(self, query, fetch=False):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

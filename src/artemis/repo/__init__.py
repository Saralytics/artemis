import os
from enum import Enum
import sqlalchemy
from abc import abstractmethod
import datetime
from contextlib import asynccontextmanager
from artemis.util import get_logger
from sqlalchemy import create_engine

logger = get_logger(__file__)


APPLICATION_DATABASE_TYPE = os.getenv("APPLICATION_DATABASE_TYPE", "postgres")
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
APPLICATION_DATABASE_URL = os.getenv(
    "APPLICATION_DATABASE_URL", f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
application_database = None


def get_application_database():
    global application_database
    if application_database is None:
        application_database_type = DatabaseType(APPLICATION_DATABASE_TYPE)
        if application_database_type == DatabaseType.POSTGRES:
            application_database = create_engine(
                APPLICATION_DATABASE_URL,
                pool_size=10,
                max_overflow=2,
                pool_recycle=300,
                pool_pre_ping=True,
                pool_use_lifo=True,
            )
    return application_database


def close_application_database():
    global application_database
    if application_database:
        application_database.close()
        application_database = None


class DatabaseType(Enum):
    POSTGRES = "postgres", True

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, is_sql=None):
        self._is_sql = is_sql

    @property
    def is_sql(self):
        return self._is_sql


class ApplicationDatabase:
    def __new__(cls):
        if cls.__name__ == "ApplicationDatabase":
            # if not DatabaseType(APPLICATION_DATABASE_TYPE).is_sql:
            #     return NoSqlApplicationDatabase()
            return SqlApplicationDatabase()
        return super().__new__(cls)


class SqlApplicationDatabase(ApplicationDatabase):
    
    def __init__(self):
        self.database_engine = get_application_database()
        with self.database_engine.begin() as conn:
            self._create_db_tables(conn)

    def _create_db_tables(self, conn):
        metadata = sqlalchemy.MetaData()
        self.example_table = sqlalchemy.Table("exampletable", metadata) #, autoload_with=conn <- this will cause issue if the table doesnt already exist


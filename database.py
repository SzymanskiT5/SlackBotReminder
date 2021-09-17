import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String, Date

class Database:
    def __init__(self):
        self.session = None
        self.base = declarative_base()
        self.config_db()

    def config_db(self):
        engine = create_engine(f'sqlite:///bot_base.db', echo=False)
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        self.session = Session()
        self.base.metadata.create_all(engine, self.base.metadata.tables.values())
        if not database_exists(engine.url):
            create_database(engine.url)

db = Database()

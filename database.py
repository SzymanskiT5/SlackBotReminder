from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database



class Database:
    def __init__(self):
        self.session = None
        self.engine = create_engine('sqlite:///bot_base.db', echo=False)
        self.base = declarative_base()
        self.config_db()

    def config_db(self) -> None:
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Session = sessionmaker(bind=self.engine)
        Session.configure(bind=self.engine)
        self.session = Session()



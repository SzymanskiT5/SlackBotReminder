from main import db
from sqlalchemy import Column, Integer, String


class Student(db.base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_month = Column(String)

    def __str__(self) -> str:
        return f'{self.name}, last message {self.last_month}'
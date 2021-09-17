from database import db
from sqlalchemy import Column, Integer, String, Date, Boolean


class Student(db.base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    #date = Column(Date)
    last_month = Column(String)

    def __str__(self):
        return f'{self.name}, last message {self.date}'
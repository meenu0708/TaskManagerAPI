from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime
from . database import Base

class TodoItem(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    priority=Column(Integer)
    due_date=Column(DateTime, default=datetime.datetime.utcnow)
    completed = Column(Boolean, default=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


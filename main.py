from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy import create_engine

DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/timbe'

engine = create_engine(DATABASE_URI)

Session = sessionmaker()

Base = declarative_base()

class Hero(Base):
    __tablename__="heroes"
    id = Column(Integer, primary_key=True)
    hero_name = Column(String(50))
    alias = Column(String(50))
    created = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"<User heroname = {self.hero_name} alias = {self.alias}>"


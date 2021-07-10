from sqlalchemy import Column, String, Integer
from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    def __repr__(self):
        return f'<Title {self.title}>'
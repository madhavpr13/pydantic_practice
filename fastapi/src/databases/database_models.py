from databases.database import Base
from sqlalchemy import Column, Integer, String, Float

class Book(Base):
    __tablename__ = "books"

    isbn = Column(String, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)
    description = Column(String)
    year_of_publication = Column(Integer)
    rating = Column(Float)

    # "isbn": "0307277674",
    # "title": "The Kite Runner",
    # "author": "Khaled Hosseini",
    # "genre": "Historical Fiction",
    # "description": "A heartfelt story of friendship and betrayal set against the backdrop of Afghanistan's turbulent history.",
    # "yearOfPublication": 2003,
    # "rating": 4.6
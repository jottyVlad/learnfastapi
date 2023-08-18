import datetime

from sqlalchemy import Column, String, DateTime, Integer, Text

from database import Base


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    author = Column(String, index=True, default="admin")

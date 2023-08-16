import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    text: str
    author: str

    class Config:
        from_attributes = True


class Article(ArticleBase):
    created_at: datetime.datetime


import datetime

from sqlalchemy.orm import Session

import models, schemas


def get_article(db: Session, article_id: int):
    return db.query(models.Article).get(article_id)


def create_article(db: Session, article: schemas.ArticleBase):
    db_article = models.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

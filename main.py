from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import database, models, services, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/articles/get/{article_id}", response_model=schemas.Article)
async def get_article(article_id: int,
                      db: Session = Depends(get_db)):
    article = services.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404)
    return article


@app.post("/articles/post/", response_model=schemas.Article)
async def add_article(
        article: schemas.ArticleBase,
        db: Session = Depends(get_db)
):
    article_ = services.create_article(db, article)

    return article_

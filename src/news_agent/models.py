from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    title: str
    url: HttpUrl
    source: str
    published_at: datetime
    summary: str = ""

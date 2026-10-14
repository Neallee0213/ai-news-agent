from datetime import UTC, datetime

from news_agent.models import Article

good = Article(
    title="New model released",
    url="https://openai.com/news/example",
    source="OpenAI",
    published_at=datetime.now(UTC),
)
print(good)

bad = Article(
    title="Broken",
    url="not a link",
    source="Test",
    published_at=datetime.now(UTC),
)

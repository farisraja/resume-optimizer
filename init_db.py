import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.models.base import Base
from app.config import get_settings

# Import all models to ensure they are registered
from app.models import user, profile, job, token_usage, tenant, roast, roast_view, credit

async def init_db():
    settings = get_settings()
    engine = create_async_engine(settings.DATABASE_URL)
    async with engine.begin() as conn:
        print("Creating tables...")
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized successfully.")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())

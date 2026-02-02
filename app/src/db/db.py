from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.settings import settings

engine = create_async_engine(
    f'postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_address}/{settings.db_name}')
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as async_session:
        yield async_session

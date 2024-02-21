import datetime

from sqlalchemy.exc import IntegrityError

from app.main.database import async_session_maker
from aiogram import types
from sqlalchemy import insert, select, update
from app.users.models import Users, FilmUsers


async def save_user(message: types.Message):
    async with async_session_maker() as session:
        user = message.from_user.username
        try:
            stmt = insert(Users).values(name=user)
            await session.execute(stmt)
            await session.commit()
            return True
        except IntegrityError:
            return False


async def search_film_user(
        id: int,
        message: types.Message
):
    async with async_session_maker() as session:
        query = select(Users).where(Users.name == message.from_user.username)
        result = await session.execute(query)
        for results in result.scalars().all():
            stmt = insert(FilmUsers).values(id_film=id, id_users=results.id)
            await session.execute(stmt)
            await session.commit()


async def update_date_activity(callback: types.CallbackQuery):
    async with async_session_maker() as session:
        update_user = update(Users).where(
            Users.name == callback.from_user.username
        ).values(
            last_activity=datetime.datetime.utcnow()
        )
        await session.execute(update_user)
        await session.commit()
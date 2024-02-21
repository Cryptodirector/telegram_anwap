from app.main.database import async_session_maker
from sqlalchemy import select
from aiogram import types
from app.main.models import Films
from app.users.service import search_film_user


async def get_current_film(message: types.Message):
    list_result = ""

    async with async_session_maker() as session:
        query = select(Films).filter(Films.title.ilike(f'%{message.text}%'))
        result = await session.execute(query)

        for results in result.scalars().all():
            print(results.id, results.title)
            list_result += f'{results.title}: {results.link}\n\n'
        await search_film_user(id=results.id, message=message)
        if list_result == "":
            return None
        return list_result


async def search_film_id(id):
    async with async_session_maker() as session:
        query = select(Films).where(Films.id == int(id))
        result = await session.execute(query)
        for results in result.scalars().all():
            return f'{results.title}🎬\n{results.link}'

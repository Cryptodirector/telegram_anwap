import asyncio

import aiohttp
from bs4 import BeautifulSoup as bs
from app.main.database import async_session_maker
from sqlalchemy import insert
from app.main.models import Films


class Parser:
    @staticmethod
    async def get_film():
        async with aiohttp.ClientSession() as session:
            for page in range(1, 72276):
                url = f'https://api.linktodo.ws/embed/movie/{page}'
                async with session.get(url) as response:

                    soup = bs(await response.text(), 'html.parser')
                    title = soup.find('title')
                    async with async_session_maker() as async_session:
                        stmt = insert(Films).values(title=title.text, link=url)
                        await async_session.execute(stmt)
                        await async_session.commit()


asyncio.run(Parser.get_film())

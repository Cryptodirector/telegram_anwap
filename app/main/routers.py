import asyncio
import os

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
from aiogram import types, Bot
from aiogram import Router, F
from aiogram.filters import Command
from app.main.keyboards import Keyboards
from app.main.service import get_current_film, search_film_id
from app.users.service import save_user, update_date_activity

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await save_user(message)
    await Keyboards.main_menu(message)


class UserMSG(StatesGroup):
    search = State()
    search_id = State()


@router.callback_query(F.data == "search_films")
async def search_film(
        callback: types.CallbackQuery,
        state: FSMContext
):
    await update_date_activity(callback)
    await state.set_state(UserMSG.search)
    delete = await callback.message.answer(
        "Напишите название фильма или сериала:",
    )
    await asyncio.sleep(10)
    await bot.delete_message(chat_id=callback.from_user.id, message_id=delete.message_id)


@router.message(UserMSG.search)
async def fun(message: types.Message, state: FSMContext):
    await message.delete()
    if len(message.text) <= 2:
        del_msg = await message.answer(text='В запросе должно быть более 2 букв!')
        await asyncio.sleep(5)
        await bot.delete_message(chat_id=message.from_user.id, message_id=del_msg.message_id)
    else:
        link = await get_current_film(message)
        builder = await Keyboards.mode_selection()
        if link is None:
            await message.answer(text='У нас такого фильма к сожалению нет!\n'
                                      'Попробуйте ввести название фильма корректно.', reply_markup=builder.as_markup())
        else:
            await message.answer(text=f'Приятного просмотра! Ваш Black Sprut!🐙🏴‍☠\n\n'
                                      f'{link}',
                                 reply_markup=builder.as_markup())
        await state.clear()


@router.callback_query(F.data == 'search_films_id')
async def search_films_id(
        callback: types.CallbackQuery,
        state: FSMContext
):
    await update_date_activity(callback)
    await state.set_state(UserMSG.search_id)

    delete = await callback.message.answer(
        "Вставьте id с ТикТока:",
    )
    await asyncio.sleep(10)
    await bot.delete_message(chat_id=callback.from_user.id, message_id=delete.message_id)


@router.message(UserMSG.search_id)
async def fun2(message: types.Message, state: FSMContext):
    await message.delete()
    builder = await Keyboards.mode_selection()
    try:

        link = await search_film_id(message.text)
        await message.answer(text=f'Приятного просмотра! Ваш Black Sprut!🐙🏴‍☠\n\n'
                                  f'{link}',
                             reply_markup=builder.as_markup())
        await state.clear()

    except ValueError:
        del_msg = await message.answer(text='Некорректные данные!')
        await asyncio.sleep(8)
        await bot.delete_message(chat_id=message.from_user.id, message_id=del_msg.message_id)


# @router.callback_query(F.data == "advertising")
# async def advertising(callback: types.CallbackQuery):
#     await callback.message.answer(
#         "Это здорово!",
#     )

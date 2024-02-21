from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Keyboards:
    builder = None

    @classmethod
    async def main_menu(
            cls,
            message: types.Message,

    ):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Поиск фильмов 🎬", callback_data="search_films")
        )

        builder.row(types.InlineKeyboardButton(
            text="Поиск фильмов по ID с ТикТока 🎬",
            callback_data="search_films_id")
        )

        builder.row(types.InlineKeyboardButton(
            text="Реклама 📣",
            callback_data="advertising")
        )

        builder.adjust(1)
        await message.answer('Привет, на связи Black Sprut 🐙🏴‍☠!\n\n'
                             'Это бесплатный бот, c огромной базой фильмов и сериалов.\n'
                             'Просто, введи название фильма или сериала, а мы постарамся его найти!😎',
                             reply_markup=builder.as_markup())
        return builder

    @classmethod
    async def mode_selection(cls):
        builder = InlineKeyboardBuilder()
        builder.row(types.InlineKeyboardButton(
            text="Найти другой фильм 🎬", callback_data="search_films")
        )
        builder.row(types.InlineKeyboardButton(
            text="Ввести id с Тиктока 🎬", callback_data="search_films_id")
        )
        return builder

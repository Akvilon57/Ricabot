from data import config
from aiogram import types
from loader import dp, bot
from keyboards.category import mas, back_menu
from datetime import datetime, timedelta

from aiogram.types import Message, CallbackQuery

@dp.callback_query_handler(text_contains='buy')
async def  chat_privat(call: CallbackQuery):
	await call.answer(cache_time=60)
	callback_data = call.data
	await call.message.answer(f'Работает {callback_data}')
	





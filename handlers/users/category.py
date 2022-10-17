from aiogram import types  
from loader import dp
from keyboards.category import menu_catalog, category, mas


@dp.message_handler(text=menu_catalog)
async def command_land(message: types.Message):
	user=mas[message.from_user.id]
	user['last_catalog'] = message.text
	await message.answer(f'➡ {message.text}', reply_markup=category(message.from_user.id, message.text))
from aiogram import types  
from loader import dp
from keyboards.category import menu_main


@dp.message_handler(text=['Главное меню','Головне меню'])
async def command_land(message: types.Message):
	await message.answer(f'➡ {message.text}', reply_markup=menu_main(message.from_user.id))
	


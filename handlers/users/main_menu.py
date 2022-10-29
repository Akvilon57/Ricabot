from aiogram import types  
from loader import dp
from keyboards.category import menu_main


@dp.message_handler(text=['Главное меню','Головне меню'])
async def command_land(message: types.Message):
	if menu_main != None:
		await message.answer(f'➡ {message.text}', reply_markup=menu_main(message.from_user.id))
	else:
		if message.from_user.language_code == 'uk': 
			await message.answer(f'/start - Запустіть бота')
		else:
			await message.answer(f'/start - Запустите бота')


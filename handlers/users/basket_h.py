from aiogram import types  
from loader import dp, bot
from keyboards.inline import basket_del_menu
from func import basket

@dp.message_handler(text=['/basket','🛒 Кошик','🛒 Корзина'])
async def  command_help(message: types.Message):
	user=str(message.from_user.id)
	if message.from_user.language_code == 'uk':
		bask=basket('Українська мова', user,'read')
		if bask:
			bas=" ".join(bask)
			await message.answer(f'{bas}', reply_markup=basket_del_menu('Українська мова', user))
		else:
			await message.answer(f"Тут поки пусто 🤔\nВідкрийте мене пізніше.")
	else:
		bask=basket('Русский язык', user,'read')
		if bask:
			bas=" ".join(bask)
			await message.answer(f'{bas}', reply_markup=basket_del_menu('Русский язык', user))
		else:
			await message.answer(f"Здесь пока пусто 🤔\nОткройте меня позже.")
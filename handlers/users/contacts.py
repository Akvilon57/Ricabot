from aiogram import types  
from loader import dp
from aiogram.utils.markdown import hlink

@dp.message_handler(text='/contacts')
async def  command_help(message: types.Message):
	if message.from_user.language_code == 'uk':
		await message.answer(f"{message.from_user.full_name}, ви можете зв'язатися з нами:\n"
			f'📞 Lifecell:  +380639958988\n'
			f'📞 Київстар:  +380988886022\n'
			f'📱 Viber:  +380639958988\n'
			f"📱 {hlink('Написати менеджеру', 'https://t.me/RicaMare_shop')}\n"
			f"📱 {hlink('Телеграмм канал', 'https://t.me/RicaMare_shops')}\n"
			f'📬 Пошта: shop@ricamare.com.ua\n'
			f"🏪 ШОУРУМ: {hlink('м.Харків, пр.Науки 3','https://goo.gl/maps/sf6ahKrJienvr7FKA')}\n")

	else:
		await message.answer(f'{message.from_user.full_name}, вы можите связаться с нами:\n'
			f'📞 Lifecell:  +380639958988\n'
			f'📞 Киевстар:  +380988886022\n'
			f'📱 Viber:  +380639958988\n'
			f"📱 {hlink('Написать менеджеру', 'https://t.me/RicaMare_shop')}\n"
			f"📱 {hlink('Телеграмм канал', 'https://t.me/RicaMare_shops')}\n"
			f'📬 Почта: shop@ricamare.com.ua\n'
			f"🏪 ШОУРУМ: {hlink('г.Харьков, пр.Науки 3','https://goo.gl/maps/sf6ahKrJienvr7FKA')}\n")


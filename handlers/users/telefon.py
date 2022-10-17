from data import config
from aiogram import types
from loader import dp, bot
from keyboards.category import mas, back_menu
from func import basket
from datetime import datetime, timedelta
from aiogram.utils.markdown import hlink,hbold,hitalic
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import admin_shop


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def  fone(message: types.Message):
	user=mas[message.from_user.id]
	lang=user['lang']
	tel=f'{message.contact.phone_number}'
	user_id=str(message.from_user.id)
	bask=basket(lang, user_id, 'del',tel)
	#print(bask)
	if bask == False:
		if lang=='Русский язык':
			await message.answer(f"Здесь пока пусто 🤔\nОткройте меня позже.")
		elif lang=='Українська мова':
			await message.answer(f"Тут поки пусто 🤔\nВідкрийте мене пізніше.")
	else:
		bas=" ".join(bask)
		if 'zak' in mas:
			mas['zak']+=1
		else:
			mas['zak']=1500
		zak=mas['zak']

		if lang=='Русский язык':
			markup_zak = types.InlineKeyboardMarkup()
			markup_zak.add(types.InlineKeyboardButton(text=f'Написать менеджеру', url='https://t.me/RicaMare_shop'))
			ir=f'Ваш заказ принят!\nНомер заказа №{zak}:\n\n'
			await bot.send_message(message.from_user.id,f"{hbold(ir)}{bas}\nВ ближайшее время с вами свяжется наш менеджер для уточнения требуемой информации.\n\n{hbold('Наши контакты:')}\n📞 Lifecell:  +380639958988\n📞 Київстар:	+380988886022",reply_markup=markup_zak)

		elif lang=='Українська мова':
			markup_zak = types.InlineKeyboardMarkup()
			markup_zak.add(types.InlineKeyboardButton(text=f'Написати менеджеру', url='https://t.me/RicaMare_shop'))
			ir=f'Ваше замовлення прийнято!\nНомер замовлення №{zak}:\n\n'
			await bot.send_message(message.from_user.id,f"{hbold(ir)}{bas}\nНайближчим часом з вами зв'яжеться наш менеджер для уточнення необхідної інформації.\n{hbold('Наші контакти:')}\n📞 Lifecell: + 380639958988\n📞 Київстар: +380988886022",reply_markup=markup_zak)
		
		today = datetime.today()
		today_data=today.strftime("%Y-%m-%d (%H.%M)")

		button_url=f"tg://user?id={message.from_user.id}"
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton(text=f'{message.from_user.full_name}', url=button_url))
		
		text=f'Номер заказа №{zak}:\n{message.from_user.full_name}: {tel}\n{bas}\nДата: {today_data}'
		await bot.send_message(admin_shop,text,reply_markup=markup)




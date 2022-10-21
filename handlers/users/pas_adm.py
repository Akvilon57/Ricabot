from aiogram import types  
from loader import dp, bot
from data.config import admin_shop, admins, slov
import asyncio

@dp.message_handler(text=slov)
async def  command_help(message: types.Message):
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:
		markup = types.InlineKeyboardMarkup(row_width = 2)
		markup.add(types.InlineKeyboardButton(text = 'Заказы', callback_data='zak'))
		markup.add(types.InlineKeyboardButton(text='Пользователи', callback_data='user'))
		markup.add(types.InlineKeyboardButton(text='Очистить статистику', callback_data='jsc'))
		await bot.send_message(message.from_user.id,'Приветствую админ.\n startmail - рассылка,\nstartskidki - рассылка скидок,\nsicapau[артикул] - отправка артикула,\n startteleg, stopteleg - отправка в группу телеграм',reply_markup=markup)


		


import logging
from  aiogram import Dispatcher
from data.config import admins

async def on_startup_notify(dp: Dispatcher):
	try:
		text = 'Бот RicaMare запущен'
		await dp.bot.send_message(chat_id=admins, text = text)
	except Exception as err:
		logging.exception(err)


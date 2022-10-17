from aiogram import types

async def set_default_commands(dp):
	await dp.bot.set_my_commands([
		types.BotCommand('start',f'🤖	 Запуск бота'),
		types.BotCommand('basket', f'🛒	 Корзина'),
		types.BotCommand('contacts',f'🎫		Контакты'),
		types.BotCommand('stop',f'📭		Прекратить рассылку'),
		])

	

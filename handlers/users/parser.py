from aiogram import types  
from loader import dp, bot
from data.config import admin_shop, admins, slov
from files.parsers import rload,ua
import asyncio
from datetime import datetime

def timepars():
	global t
	s=datetime.now()
	start = 3
	x,y =int(s.hour),int(s.minute)
	h=24+start-x
	if y>0:
		t=(h - 1)*3600+(60 - y)*60						
	else:
		t=h*3600
	return t









async def eternity():
	print('st')
	await asyncio.sleep(120)
	print('yay!')

async def mains_timer():
		try:
			await asyncio.wait_for(eternity(), timeout=10)
			
		except asyncio.TimeoutError:
			print('fack')
			pass



@dp.message_handler(text=['parser_start','parser_stop'])
async def  command_help(message: types.Message):
	global tik, key
	#user=[str(admin_shop),str(admins)]
	#if str(message.from_user.id) in user:
	print(message.text)
	key=True
	if message.text=='parser_stop':
		key=False
		await bot.send_message(message.from_user.id,'Парсер остановлен')

	if message.text=='parser_start':

		tik=timepars()

		while key:
			await bot.send_message(message.from_user.id,f'Парсер запущен, обновление произойдет через {tik/3600} часов')
			await asyncio.sleep(tik)
			try:
				rload()
				await bot.send_message(message.from_user.id,'Базы успешно обновлены')
				tik=timepars()+175680
			except Exception as a:
				await bot.send_message(message.from_user.id,f'У нас ошибка в обновлении базы: \n\n {a}\n\nПерезапуск через 2 мин')
				await asyncio.sleep(20)
				await bot.send_message(message.from_user.id,'Перезапуск парсера')
				try:
					rload()
					await bot.send_message(message.from_user.id,'Базы успешно обновлены')
				except Exception as a:
					await bot.send_message(message.from_user.id,f'У нас ошибка в обновлении базы: \n\n {a}')
					await bot.send_message(message.from_user.id,f'Следующие обновление через 3 дня')
					tik=timepars()+175680

	




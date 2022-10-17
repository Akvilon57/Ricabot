from aiogram import types  
from loader import dp, bot
from keyboards.category import catalog
from data.config import JRASS
import datetime
import json
from utils.misc import rate_limit



@rate_limit(limit=5)
@dp.message_handler(text=['/stop','/stop@Serda2_bot'])


async def  command_stop(message: types.Message):

	if message.from_user.language_code == 'uk':
		await message.answer(f'Ваш обліковий запис успішно відписаний від розсилки.')
	else:
		await message.answer(f'Ваш аккаунт успешно отписан от рассылки.')
	

	#Записываем юзера в базу

	with open(JRASS, 'r+',encoding='utf-8') as fi:
		datas = json.load(fi)
		

# 	Добавление в usermail
		datau=datas['usermail']
		use=str(message.from_user.id)
		datau[use]=0


		fi.seek(0)
		fi.truncate(0)
		json.dump(datas, fi)
		fi.close()

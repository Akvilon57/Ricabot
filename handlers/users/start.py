from asyncio import sleep
import asyncio
from aiogram import types  
from loader import dp, bot
from keyboards.category import catalog
from data.config import JRASS, GROUP
import datetime
import json
from utils.misc import rate_limit




@rate_limit(limit=5)


@dp.message_handler(text=['/start','/start@RicamareBot'])


async def  command_start(message: types.Message):


	if message.from_user.language_code == 'uk':
		await message.answer(f'Оберіть категорію:', reply_markup=catalog(message.from_user.id,'Українська мова'))
	else:
		await message.answer(f'Выберите категорию:', reply_markup=catalog(message.from_user.id,'Русский язык'))
	#print(message.from_user)

	#Записываем юзера в базу
	today = datetime.datetime.today()
	today_data=today.strftime("%Y-%m-%d-%H-%M")
	with open(JRASS, 'r+',encoding='utf-8') as fi:
		datas = json.load(fi)
		if 'users' not in datas.keys():
			datas['users']={}
		if 'usermail' not in datas.keys():
			datas['usermail']={}

# 	Добавление в users
		datau=datas['users']
		use=str(message.from_user.id)
		if use in datau:
			user=datau[use]
			dlin=len(user)
			if dlin < 5: 
				user.append(today_data)
			elif dlin == 5:
				user.pop(0)
				user.append(today_data)
		else:
			datau[use]=[]
			user=datau[use]
			user.append(today_data)

# 	Добавление в usermail
		datau=datas['usermail']
		use=str(message.from_user.id)
		datau[use]=1


		fi.seek(0)
		fi.truncate(0)
		json.dump(datas, fi)
		fi.close()






	#s=await bot.get_chat(GROUP) # Описание группы
	#s=await bot.get_chat_members_count(GROUP) # Количество участников в группе
	#s=await bot.get_chat_member(GROUP, message.from_user.id) # Информация по члену группы
	

	#s={f'{message.from_user.username},{message.chat.id}':1}
	#for key in s.keys():
	#	if str(message.chat.id) in key:
	#		print(s)
	
	#s=bot.https://core.teleg("-1001166920463")


#@dp.message_handler(content_types=["new_chat_members"])
#async def handler_new_member(message):
#	print(message.new_chat_members[0])
#	first_name = message.new_chat_members[0].first_name
#	await bot.send_message(message.chat.id,'hi')


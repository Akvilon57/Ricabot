from aiogram import types  
from aiogram.dispatcher import filters
from loader import dp, bot
from aiogram.utils.markdown import hbold, hcode, hlink
from data.config import admin_shop, admins, slov
import asyncio
import random
import json
from urllib.request import urlopen
from datetime import datetime
from data.config import JRASS, JLZ, admin_shop,admins,A,GROUPTELE
from utils.misc import rate_limit



fotos = {}

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
	user=[str(admin_shop),str(admins),str(A)]
	if str(message.from_user.id) in user:
		global fotos
		if 'foto' not in fotos:
			fotos['foto']=[]
		spis=fotos['foto']
		spis.append(message.photo[-1].file_id)

		if message.caption != None:
			fotos['text']=message.caption
		else:
			if 'text' not in fotos:
				fotos['text']=None
		await bot.send_photo(admins, message.photo[-1].file_id,caption=message.caption)
		await message.answer('Фото добавленo, введите  : startfoto')
	else:
		await message.answer('Команда {message.text} не найдена.')



@dp.message_handler(text=['startfoto','sendfoto','userfoto','sendall'])
async def  start_m(message: types.Message):
	global fotos
	user=[str(admin_shop),str(admins),str(A)]
	if str(message.from_user.id) in user:
		if len(fotos['foto'])>0:
			if message.text == 'startfoto':

				foto = fotos['foto']
				text = fotos['text']
				dlin = len(foto)
				i = 1
				while True:
					if i == 1 and dlin > 0:
						media =types.MediaGroup()
						f= foto[i - 1]
						media.attach_photo(f, text)
						i += 1
					elif dlin >= i and dlin > 0:
						f = foto[i - 1]
						#f = open(foto[i - 1], 'rb')
						media.attach_photo(f)
						i += 1
					else:
						i = 1
						break
							
				await bot.send_media_group(admins, media=media)
				await message.answer('clearfoto - удалить фото\nsendfoto - отправить фото в группу\nuserfoto - фото юзерам\nsendall - отправить юзерам и в группу')

		
			if message.text in ['sendfoto','sendall','userfoto']: 
				foto = fotos['foto']
				text = fotos['text']
				dlin = len(foto)
				i = 1
				while True:
					if i == 1 and dlin > 0:
						media =types.MediaGroup()
						f= foto[i - 1]
						media.attach_photo(f, text)
						i += 1
					elif dlin >= i and dlin > 0:
						f = foto[i - 1]
						#f = open(foto[i - 1], 'rb')
						media.attach_photo(f)
						i += 1
					else:
						i = 1
						break
				if message.text in ['sendfoto','sendall']:			
					await bot.send_media_group(GROUPTELE, media=media)
				if message.text in ['userfoto','sendall']:
					await message.answer('Отправляю....')
					allsend=0
					with open(JRASS, 'r',encoding='utf-8') as fi:
						datas = json.load(fi)
						usersmail=datas['usermail']
						for user,value in usersmail.items():
							if value == 1:
								print(user)
								try:
									await bot.send_media_group(str(user), media=media)
									allsend+=1
								except Exception:
									pass
								await asyncio.sleep(10)
						fi.close()
						await message.answer('Фото отправлено {allsend} человек')
				fotos={}
				await message.answer('Фото удалено из памяти')
		else:
			await message.answer('В памяти нет фото. Добавте :-)')

			
@dp.message_handler(text='clearfoto')
async def  start_m(message: types.Message):
	global fotos
	
	user=[str(admin_shop),str(admins),str(A)]
	if str(message.from_user.id) in user:
		fotos={}
		await message.answer('Фото удалено из памяти')



					






		






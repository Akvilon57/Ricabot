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
from data.config import JRASS, JLZ

from utils.misc import rate_limit


def timepars(days=0):
	global t
	s=datetime.now()
	start = 11
	x,y =int(s.hour),int(s.minute)
	h=(days*24)+24+start-x
	if y>0:
		t=(h - 1)*3600+(60 - y)*60						
	else:
		t=h*3600
	return t


@rate_limit(limit=5)


@dp.message_handler(text=['startmail','startskidki'])
async def  start_m(message: types.Message):
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:
		mail = message.text
		while True:
			sezon=''
			today =  datetime.today()
			month= int(today.strftime("%m"))
			if month>8 or month<3:
				sezon='zima'
			else:
				sezon='leto'

			with open(JLZ, 'r', encoding='utf-8') as file:
				infa = json.load(file)
				sez = infa[sezon]
				cart=''
				

				if mail == 'startmail':
					k= sez[random.randint(0, len(infa[sezon])-1)]
					arti=f"Артикул: {k['articul']}"
					otpiska = f"{hlink('Отписаться от рассылки', 'https://t.me/RicamareBot/stop')}\n"
					tele = f"{hlink('Телеграмм канал', 'https://t.me/RicaMare_shops')}"
					opis=''
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold('Опис: ')}{k['opisanie']}\n "
					
					sklad=''
					if k['sostav'] !='':		
						if k['sostav'] !=':':
							if k['sostav'] !=': ':
								sklad=f"{hbold('Слад: ')}{k['sostav']}\n\n"

					cart = f"{hlink(arti, k['urls'])}\n{hbold('Цiна: ')}{hbold(k['price_new'])}\n\n{sklad}{opis}{otpiska}https://t.me/RicaMare_shops"

				elif mail == 'startskidki':
					price_old=''
					while True:
						k= sez[random.randint(0, len(infa[sezon])-1)]
						if k['price_old'] !='':
							if k['price_old'] != None:
								price_old=f"{hbold('Цiна: ')}<s>{k['price_old']}</s>"
								break
					arti=f"Артикул: {k['articul']}"
					otpiska = f"{hlink('Отписаться от рассылки', 'https://t.me/RicamareBot/stop')}\n"
					tele = f"{hlink('Телеграмм канал', 'https://t.me/RicaMare_shops')}"
					opis=''
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold('Опис: ')}{k['opisanie']}\n "
					
					sklad=''
					if k['sostav'] !='':		
						if k['sostav'] !=':':
							if k['sostav'] !=': ':
								sklad=f"{hbold('Слад: ')}{k['sostav']}\n\n"
					
					cart = f"{hlink(arti, k['urls'])}\n{price_old}\n{hbold('Цiна: ')}<a style='color:#FF0000'>{k['price_new']}</a>\n\n{sklad}{opis}{otpiska}https://t.me/RicaMare_shops"




				foto=k['foto']
				dlin = len(foto)
				i = 1
				while True:
					if i == 1 and dlin > 0:
						media =types.MediaGroup()
						f= urlopen(foto[i - 1])
						media.attach_photo(types.InputFile(f), cart)
						i += 1
					elif dlin >= i and dlin > 0:
						f = urlopen(foto[i - 1])
						#f = open(foto[i - 1], 'rb')
						media.attach_photo(types.InputFile(f))
						i += 1
					else:
						i = 1
						break
				
				with open(JRASS, 'r',encoding='utf-8') as fi:
					datas = json.load(fi)
					usersmail=datas['usermail']
					for user,value in usersmail.items():
						if value == 1:
							await bot.send_media_group(user, media=media)
					fi.close()
				
				file.close()
				await asyncio.sleep(10)


	
@dp.message_handler(filters.Text(contains='sicapau', ignore_case=True))
async def stop_m(message: types.Message):
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:
		k=''
		art=message.text.upper().replace('SICAPAU','').strip()
		print(art)
		with open(JLZ, 'r', encoding='utf-8') as file:
			infa = json.load(file)
			for tov in infa.values():
				for cart in tov:
					if art in cart['articul']:
						k=cart
			if k !='':
				price_new='Цiна: '
				price_old='\n'
				if k['price_old'] !='':
					if k['price_old'] != None:
						price_old=f"\nПовна цiна: <s>{k['price_old']}</s>\n"
						price_new='Акційна ціна: '
				arti=f"Артикул: {k['articul']}"
				otpiska = f"{hlink('Отписаться от рассылки', 'https://t.me/RicamareBot/stop')}\n"
				tele = f"{hlink('Телеграмм чат:', 'https://t.me/+FzUwcj5hV_lmZDUy')}"
				opis=''
				if k['opisanie'] !='':		
					if k['opisanie'] !=':':
						if k['opisanie'] != None: 
							opis=f"{hbold('Опис: ')}{k['opisanie']}\n "
						
				sklad=''
				if k['sostav'] !='':		
					if k['sostav'] !=':':
						if k['sostav'] !=': ':
							sklad=f"{hbold('Слад: ')}{k['sostav']}\n\n"
						
				cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{sklad}{opis}{otpiska}https://t.me/RicaMare_shops"




				foto=k['foto']
				dlin = len(foto)
				i = 1
				while True:
					if i == 1 and dlin > 0:
						media =types.MediaGroup()
						f= urlopen(foto[i - 1])
						media.attach_photo(types.InputFile(f), cart)
						i += 1
					elif dlin >= i and dlin > 0:
						f = urlopen(foto[i - 1])
						#f = open(foto[i - 1], 'rb')
						media.attach_photo(types.InputFile(f))
						i += 1
					else:
						i = 1
						break
				
				with open(JRASS, 'r',encoding='utf-8') as fi:
					datas = json.load(fi)
					usersmail=datas['usermail']
					for user,value in usersmail.items():
						if value == 1:
							await bot.send_media_group(user, media=media)
					fi.close()
				file.close()
			
			else:
				await message.answer(f'Такой позиции нет ;(')	







@dp.message_handler(text=['startteleg','stopteleg'])
async def  start_m(message: types.Message):
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:	
		global medias,foto
		mail = message.text
		while True:
			t=timepars()
			
			sezon=''
			today =  datetime.today()
			month= int(today.strftime("%m"))
			if month>8 or month<3:
				sezon='zima'
			else:
				sezon='leto'

			with open(JLZ, 'r', encoding='utf-8') as file:
				infa = json.load(file)
				sez = infa[sezon]
				cart=''
				

				if mail == 'startteleg':
					await asyncio.sleep(t)
					k= sez[random.randint(0, len(infa[sezon])-1)]
					arti=f"Артикул: {k['articul']}"
					otpiska = f"{hlink('🤖RicamareBot    ', 'https://t.me/RicamareBot')}"
					tele = f"{hlink('📱Менеджер', 'https://t.me/RicaMare_shop')}"
					opis=''
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold('Опис: ')}{k['opisanie']}\n "
					
					sklad=''
					if k['sostav'] !='':		
						if k['sostav'] !=':':
							if k['sostav'] !=': ':
								sklad=f"{hbold('Слад: ')}{k['sostav']}\n\n"

					cart = f"{hlink(arti, k['urls'])}\n{hbold('Цiна: ')}{hbold(k['price_new'])}\n\n{sklad}{opis}{otpiska}{tele}"

					
				try:
					foto=k['foto']
				except Exception as e:
					print(f'{e}')	
				dlin = len(foto)
				i = 1
				while True:
					if i == 1 and dlin > 0:
						medias =types.MediaGroup()
						f= urlopen(foto[i - 1])
						medias.attach_photo(types.InputFile(f), cart)
						i += 1
					elif dlin >= i and dlin > 0:
						f = urlopen(foto[i - 1])
						#f = open(foto[i - 1], 'rb')
						medias.attach_photo(types.InputFile(f))
						i += 1
					else:
						i = 1
						break
				
				
				try:
					await bot.send_media_group('-1001693280958', media=medias)
					await asyncio.sleep(60)
				except Exception:
					pass
				if mail == 'stopteleg':
					break			
				


						
		
		












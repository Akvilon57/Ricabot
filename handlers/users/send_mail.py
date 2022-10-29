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
from data.config import JRASS, JLZ, GROUPTELE
from utils.misc import rate_limit


def timepars(days=0):
	global t
	s=datetime.now()
	start = 8
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
	global media
	slova=['Ціна: ','Повна ціна: ','Акційна ціна🔥: ','Склад: ','Опис: ']
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
					otpiska = f"🤖@RicamareBot   "
					tele = f"{hlink('📱Телеграмм', 'https://t.me/RicaMare_shops')}"
					opis=''
					price_new=slova[0]
					price_old='\n'
			
					if k['price_old'] !='':
						if k['price_old'] != None:
							price_old = f"\n{slova[1]}<s>{k['price_old']}</s>\n"
							price_new = slova[2]
					
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold(slova[4])}{k['opisanie']}\n "


					if len(k['sostav'])<3:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{opis}{otpiska}{tele}"
					else:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{hbold(slova[3])}{k['sostav']}\n\n{opis}{otpiska}{tele}"
				elif mail == 'startskidki':
					price_old=''
					while True:
						k= sez[random.randint(0, len(infa[sezon])-1)]
						if k['price_old'] !='':
							if k['price_old'] != None:
								price_old=f"{hbold('Цiна: ')}<s>{k['price_old']}</s>"
								break
					arti=f"Артикул: {k['articul']}"
					otpiska = f"🤖@RicamareBot   "
					tele = f"{hlink('📱Телеграмм', 'https://t.me/RicaMare_shops')}"
					opis=''
					price_new=slova[0]
					price_old='\n'
			
					if k['price_old'] !='':
						if k['price_old'] != None:
							price_old = f"\n{slova[1]}<s>{k['price_old']}</s>\n"
							price_new = slova[2]
					
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold(slova[4])}{k['opisanie']}\n "


					if len(k['sostav'])<3:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{opis}{otpiska}{tele}"
					else:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{hbold(slova[3])}{k['sostav']}\n\n{opis}{otpiska}{tele}"



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
							try:
								await bot.send_media_group(user, media=media)
							except Exception as ed:
								print(f'{user}:{ed}')
					fi.close()
				
				file.close()
				


	
@dp.message_handler(filters.Text(contains='sicapau', ignore_case=True))
async def stop_m(message: types.Message):
	slova=['Ціна: ','Повна ціна: ','Акційна ціна🔥: ','Склад: ', 'Опис: ']
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:
		k=''
		art=message.text.upper().replace('SICAPAU','').strip()
		#print(art)
		with open(JLZ, 'r', encoding='utf-8') as file:
			infa = json.load(file)
			for tov in infa.values():
				for cart in tov:
					if art in cart['articul']:
						k=cart
			if k !='':
				arti=f"Артикул: {k['articul']}"
				otpiska = f"🤖@RicamareBot   "
				tele = f"{hlink('📱Телеграмм', 'https://t.me/RicaMare_shops')}"
				opis=''
				price_new=slova[0]
				price_old='\n'
			
				if k['price_old'] !='':
					if k['price_old'] != None:
						price_old = f"\n{slova[1]}<s>{k['price_old']}</s>\n"
						price_new = slova[2]
					
				if k['opisanie'] !='':		
					if k['opisanie'] !=':':
						if k['opisanie'] != None:
							opis=f"{hbold(slova[4])}{k['opisanie']}\n"


				if len(k['sostav'])<3:
					cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{opis}{otpiska}{tele}"
				else:
					cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{hbold(slova[3])}{k['sostav']}\n\n{opis}{otpiska}{tele}"



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

				await bot.send_media_group(GROUPTELE, media=media)

				with open(JRASS, 'r',encoding='utf-8') as fi:
					datas = json.load(fi)
					usersmail=datas['usermail']
					for user,value in usersmail.items():
						if value == 1:
							try:
								await bot.send_media_group(user, media=media)
							except Exception as er:
								print(f"{user}:{er}")

					fi.close()
				file.close()
			
			else:
				await message.answer(f'Такой позиции нет ;(')	







@dp.message_handler(text=['startteleg','stopteleg'])
async def  start_m(message: types.Message):
	slova=['Ціна: ','Повна ціна: ','Акційна ціна🔥: ','Склад: ','Опис: ']
	user=[str(admin_shop),str(admins)]
	if str(message.from_user.id) in user:	
		global medias,foto
		mail = message.text
		prov=True
		if mail=='stopteleg':
			prov=False
			
		while prov:
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
					
					k= sez[random.randint(0, len(infa[sezon])-1)]
					arti=f"Артикул: {k['articul']}"
					otpiska = f"🤖@RicamareBot   "
					tele = f"{hlink('📱Менеджер', 'https://t.me/RicaMare_shop')}"
					opis=''
					price_new=slova[0]
					price_old='\n'
			
					if k['price_old'] !='':
						if k['price_old'] != None:
							price_old = f"\n{slova[1]}<s>{k['price_old']}</s>\n"
							price_new = slova[2]
					
					if k['opisanie'] !='':		
						if k['opisanie'] !=':':
							if k['opisanie'] != None: 
								opis=f"{hbold(slova[4])}{k['opisanie']}\n "


					if len(k['sostav'])<3:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{opis}{otpiska}{tele}"
					else:
						cart = f"{hlink(arti, k['urls'])}{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n{hbold(slova[3])}{k['sostav']}\n\n{opis}{otpiska}{tele}"




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
					await bot.send_media_group(GROUPTELE, media=medias)
				except Exception as da:
					print(da)
				await asyncio.sleep(t)

		await message.answer(f'Рассылка на канал остановлена.')
				
				

				


						
		
		












from aiogram import types
from aiogram.utils.markdown import hbold, hcode, hlink
from loader import dp, bot
from func import lang_bot
from keyboards.inline import menu_iline
from keyboards.category import menu_category, mas, back_menu
from keyboards.default import menu_main
import json
from urllib.request import urlopen


@dp.message_handler(text = menu_category)
async def cart_product(message: types.Message):
	#await perehod_cat(message.from_user.id,message.text)
	if menu_main != None:
		global slova
		user=mas[message.from_user.id]
		user['last_category'] = message.text
		user['numb_category'] = 1
		lang=user['lang']
		catalog=user['last_catalog']
		#print(mas)
		#await message.answer(mas,reply_markup=back_menu(message.from_user.id))
		#---------------------------------------------
		#media = types.MediaGroup()
		

		infa=lang_bot(lang)
		category=infa[catalog]
		carts=category[message.text]


		st=''
		st_catalog=0
		st_categor=0
		for inf in infa:
			if inf==catalog:
				for catt in category:
					if catt==message.text:
						st=st_catalog
						#print(catt,st)
						#print(inf,st_categor)
						break
					else:
						st_categor+=1
			else:
				st_catalog+=1

		#for k in carts:
		cart_dlin=len(carts)
		if cart_dlin >0:
			k=carts[0]
			cart=''
			slova=['Цена: ','Полная цена: ','Акционная цена🔥: ','Состав: ']
			if lang=='Українська мова':
				slova=['Ціна: ','Повна ціна: ','Акційна ціна🔥: ','Склад: ']
			
			price_new=slova[0]
			price_old='\n'
			if k['price_old'] !='':
				if k['price_old'] != None:
						price_old = f"\n{slova[1]}<s>{k['price_old']}</s>\n"
						price_new = slova[2]

			if len(k['sostav'])<3:
				cart = f"{hlink(k['articul'], k['urls'])}" \
					f"{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n"
			else:
				cart = f"{hlink(k['articul'], k['urls'])}" \
				f"{price_old}{hbold(price_new)}{hbold(k['price_new'])}\n\n" \
				f"{hbold(slova[3])}{k['sostav']}\n"

			foto=k['foto']
			
			await bot.send_photo(message.chat.id, photo=foto[0], caption=cart, reply_markup=menu_iline(lang,st,st_categor,0))
			await message.answer(f'➡ {message.text}', reply_markup=menu_main(lang))

	else:
		if message.from_user.language_code == 'uk': 
			await message.answer(f'/start - Запустіть бота')
		else:
			await message.answer(f'/start - Запустите бота')
	#---------------------------------------------
	


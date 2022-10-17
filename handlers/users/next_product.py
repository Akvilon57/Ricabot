from aiogram import types
from aiogram.utils.markdown import hbold, hcode, hlink
from loader import dp, bot
from func import lang_bot
from keyboards.inline import menu_iline
from keyboards.category import category, mas, back_menu
import json
from urllib.request import urlopen


@dp.message_handler(text = ['Показать еще','Показати ще'])
async def  cart_product(message: types.Message):
	#await perehod_cat(message.from_user.id,message.text)
	user=mas[message.from_user.id]
	categ=user['last_category']
	lang=user['lang']
	catalog=user['last_catalog']
	print(mas)
	
	#---------------------------------------------
	#media = types.MediaGroup()
	
	infa=lang_bot(lang)
	categorys=infa[catalog]
	carts=categorys[categ]
	cart_dlin=len(carts)

	st_catalog=0
	st_categor=0
	for inf in infa:
		if inf==catalog:
			for catt in categorys:
				if catt==categ:
					print(catt,st_categor)
					print(inf,st_categor)
					break
				else:
					st_categor+=1
		else:
			st_catalog+=1

	




	print(cart_dlin)
	if cart_dlin > user['numb_category']:
	
		numb_cart=user['numb_category']
		k=carts[numb_cart]
		art=k['articul']
		cart = f"{hlink(k['articul'], k['urls'])}\n" \
		f"{hbold('Цена:')}{hbold(k['price_new'])}\n\n" \
		f"{hcode('Состав:')}{k['sostav']}\n"
		foto=k['foto']
		

		cartm=numb_cart-1
		await bot.send_photo(message.chat.id, photo=foto[0], caption=cart, reply_markup=menu_iline(st_catalog,st_categor,cartm))

	#---------------------------------------------
		user['numb_category'] +=1
		
	else:
		if lang=='Русский язык': 
			await message.answer('Вы, просмотрели весь товар из этой категории. Можите выбрать другую.',reply_markup=category(message.from_user.id,catalog))
		elif lang=='Українська мова':
			await message.answer(f'Ви переглянули весь товар з цієї категорії. Можна вибрати іншу.',reply_markup=category(message.from_user.id,catalog))
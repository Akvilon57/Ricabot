from aiogram import types
from aiogram.utils.markdown import hbold, hcode, hlink
from loader import dp, bot
from keyboards.inline import ikb_menu, ikb_menu_produckt_ru, menu_iline
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
	media = types.MediaGroup()
	
	if lang=='Русский язык':
		with open('files/ricamare_ru.json', 'r', encoding='utf-8') as file:
			infa = json.load(file)
	elif lang=='Українська мова':
		with open('files/ricamare_ua.json', 'r', encoding='utf-8') as file:
			infa = json.load(file)
	
	categorys=infa[catalog]
	carts=categorys[categ]
	cart_dlin=len(carts)
	print(cart_dlin)
	if cart_dlin > user['numb_category']:
	
		numb_cart=user['numb_category']
		k=carts[numb_cart]
		art=k['articul']
		cart = f"{hlink(k['articul'], k['urls'])}\n" \
		f"{hbold('Цена:')}{hbold(k['price_new'])}\n\n" \
		f"{hcode('Состав:')}{hcode({k['sostav']})}\n"

    #foto = ['new/1.JPG','new/2.JPG','new/3.JPG','new/4.JPG']
		foto=k['foto']
		dlin = len(foto)
		i = 1
		while True:
			if i == 1 and dlin > 0:
				media = types.MediaGroup()
				f=urlopen(foto[i - 1])
				#f = open(foto[i - 1], 'rb')
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
    #media.attach_photo(types.InputFile(resp1))
		#await message.answer(mas,reply_markup=back_menu(message.from_user.id))
		await bot.send_media_group(message.chat.id, media=media)

	#---------------------------------------------
		user['numb_category'] +=1
		
		await message.answer(f'Тут наш товар разный приразный',reply_markup=menu_iline(last_category,last_catalog,art))
	else:
		if lang=='Русский язык': 
			await message.answer('Вы, просмотрели весь товар из этой категории. Можите выбрать другую.',reply_markup=category(message.from_user.id,catalog))
		elif lang=='Українська мова':
			await message.answer(f'Ви переглянули весь товар з цієї категорії. Можна вибрати іншу.',reply_markup=category(message.from_user.id,catalog))
from aiogram import types
from aiogram.utils.markdown import hbold, hcode, hlink
from loader import dp, bot
#from keyboards.inline import ikb_menu, ikb_menu_produckt_ru
from keyboards.category import menu_category, mas, back_menu
import json
from urllib.request import urlopen


@dp.message_handler(text = menu_category)
async def cart_product(message: types.Message):
	#await perehod_cat(message.from_user.id,message.text)
	user=mas[message.from_user.id]
	user['last_category'] = message.text
	user['numb_category'] = 1
	lang=user['lang']
	catalog=user['last_catalog']
	print(mas)
	await message.answer(mas,reply_markup=back_menu(message.from_user.id))
	#---------------------------------------------
	media = types.MediaGroup()
	
	if lang=='Русский язык':
		with open('files/ricamare_ru.json', 'r', encoding='utf-8') as file:
			infa = json.load(file)
	elif lang=='Українська мова':
		with open('files/ricamare_ua.json', 'r', encoding='utf-8') as file:
			infa = json.load(file)
	
	category=infa[catalog]
	carts=category[message.text]
	#for k in carts:
	cart_dlin=len(carts)
	if cart_dlin >0:
		k=carts[0]
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
		await bot.send_media_group(message.chat.id, media=media)

	#---------------------------------------------
	#await message.answer(f'Тут наш товар разный приразный',reply_markup=ikb_menu)


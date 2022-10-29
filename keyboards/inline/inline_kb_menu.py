from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from data.config import admin_shop


def menu_del(lang,articul_id,size_id,price):
	menu=''
	if lang=='Русский язык':
		menu = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = '🛒		Корзина', callback_data='basket'),
					InlineKeyboardButton(text = '✅		Оформить', callback_data='ok')
				],
				[
					InlineKeyboardButton(text = f'❌			Удалить {articul_id.upper()}', callback_data=f'del {articul_id} {size_id} {price}')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показать еще', callback_data='next')
				]
				])
	if lang=='Українська мова':
		menu = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = '🛒		Кошик', callback_data='basket'),
					InlineKeyboardButton(text = '✅		Оформити', callback_data='ok')
				],
				[
					InlineKeyboardButton(text = f'❌			Вилучити {articul_id.upper()}', callback_data=f'del {articul_id} {size_id} {price}')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показати ще', callback_data='next')
				]
				])
	return menu

def menu_iline(lang,last_category,last_catalog,cart):
	ikb_menu_produckt_ru=''
	if lang=='Русский язык':
		ikb_menu_produckt_ru = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = 'Цвет и размер', callback_data=f'col {last_category} {last_catalog} {cart}')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показать еще', callback_data='next')
				]
				])
	elif lang=='Українська мова':
		ikb_menu_produckt_ru = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = 'Колір та розмір', callback_data=f'col {last_category} {last_catalog} {cart}')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показати ще', callback_data='next')
				]
				])
	return ikb_menu_produckt_ru


def menu_iline2(lang,infa_cart,size,articul,price):
	ikb_menu_produckt_ru=''

	if lang=='Русский язык':
		menu_low=[InlineKeyboardButton(text = 'Назад', callback_data='back'),InlineKeyboardButton(text = 'Показать еще',callback_data='next')]
		d=[]
		for inline in size:
			sizes=''.join(inline.split())
			sin=InlineKeyboardButton(text = inline.replace(',','').replace('&quot','').title(), callback_data=f'{infa_cart} {articul} {price} {sizes}')
			d.append(sin)
		stok=len(size)//2
		ost=len(size)%2

		masiv=[]
		if stok>0:
			for i in range(stok):
				if i==0:
					masiv.append([d[i],d[i+1]])
				elif i>0:
					masiv.append([d[2*i],d[2*i+1]])
			if ost>0:
				if ost==1:
					masiv.append([d[2*(i+1)]])       
		elif stok==0:
			if ost>0:
				if ost==1:
					masiv.append([d[0]])

		masiv.append(menu_low)
		ikb_menu_produckt_ru = InlineKeyboardMarkup(row_width = 2, inline_keyboard = masiv)
		
	elif lang=='Українська мова':
		menu_low=[InlineKeyboardButton(text = 'Назад', callback_data='back'),InlineKeyboardButton(text = 'Показати ще',callback_data='next')]
		d=[]
		for inline in size:
			sizes=''.join(inline.split())
			sin=InlineKeyboardButton(text = inline.replace(',','').replace('&quot','').title(), callback_data=f'{infa_cart} {articul} {price} {sizes}')
			d.append(sin)
		stok=len(size)//2
		ost=len(size)%2

		masiv=[]
		if stok>0:
			for i in range(stok):
				if i==0:
					masiv.append([d[i],d[i+1]])
				elif i>0:
					masiv.append([d[2*i],d[2*i+1]])
			if ost>0:
				if ost==1:
					masiv.append([d[2*(i+1)]])       
		elif stok==0:
			if ost>0:
				if ost==1:
					masiv.append([d[0]])

		masiv.append(menu_low)
		ikb_menu_produckt_ru = InlineKeyboardMarkup(row_width = 2, inline_keyboard = masiv)
		
	return ikb_menu_produckt_ru



def menu_basket_eror(lang):
	basket=''
	if lang=='Русский язык':
		basket = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = '♻ Очистить корзину', callback_data='clear'),
					InlineKeyboardButton(text = '🛒 Корзина', callback_data='basket')
				],
				[
					InlineKeyboardButton(text = 'Задать вопрос', url='https://t.me/RicaMare_shop')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показать еще', callback_data='next')
				]
				])
	elif lang=='Українська мова':
		basket = InlineKeyboardMarkup(row_width = 2,
			inline_keyboard = [
				[
					InlineKeyboardButton(text = '♻ Очистити кошик', callback_data='clear'),
					InlineKeyboardButton(text = '🛒 Кошик', callback_data='basket')
				],
				[
					InlineKeyboardButton(text = 'Задати питання', url=f'https://t.me/RicaMare_shop')
				],
				[
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показати ще', callback_data='next')
				]
				])
	return basket



def basket_del_menu(lang,user):
	import json
	from data.config import JBASK
	spis=[]
	with open(JBASK, 'r+',encoding='utf-8') as file:
		datas = json.load(file)
		if lang=='Русский язык':
			spis.append([
					InlineKeyboardButton(text = '♻ Очистить корзину', callback_data='clear'),
					InlineKeyboardButton(text = '✅		Оформить', callback_data='ok')
				])
			spis.append([
					InlineKeyboardButton(text = '🛒 Обновить корзину', callback_data='basket')
				])

			articuls=datas[user]
			for articul in articuls:
				tov=articuls[articul]
				for poz in tov:
					if poz != 'price':
						cen=tov['price']
						sin=[InlineKeyboardButton(text = f'❌ Удалить {articul.upper()} ({poz.title()})', callback_data=f'del {articul} {poz} {cen}')]
						spis.append(sin)
			spis.append([
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показать еще', callback_data='next')
				])

			menu = InlineKeyboardMarkup(row_width = 2, inline_keyboard = spis )
			file.close()
			return menu

		elif lang =='Українська мова':
			spis.append([
					InlineKeyboardButton(text = '♻ Очистити кошик', callback_data='clear'),
					InlineKeyboardButton(text = '✅		Оформити', callback_data='ok')
				])
			spis.append([
					InlineKeyboardButton(text = '🛒 Оновити кошик', callback_data='basket')
				])

			articuls=datas[user]
			for articul in articuls:
				tov=articuls[articul]
				for poz in tov:
					if poz != 'price':
						cen=tov['price']
						sin=[InlineKeyboardButton(text = f'❌ Вилучити {articul.upper()} ({poz.title()})', callback_data=f'del {articul} {poz} {cen}')]
						spis.append(sin)
			spis.append([
					InlineKeyboardButton(text = 'Назад', callback_data='back'),
					InlineKeyboardButton(text = 'Показати ще', callback_data='next')
				])

			menu = InlineKeyboardMarkup(row_width = 2, inline_keyboard = spis )
			file.close()
			return menu
















ikb_menu_produckt_ru = InlineKeyboardMarkup(row_width = 2,
	inline_keyboard = [
		[
			InlineKeyboardButton(text = 'Добавить в корзину', callback_data='add'),
			InlineKeyboardButton(text = 'Удалить с корзины', callback_data='delete')
		],
		[
			InlineKeyboardButton(text = 'Корзина', callback_data='bag'),
			InlineKeyboardButton(text = 'Цвет и размер', callback_data='color_size')
		],
		[
			InlineKeyboardButton(text = 'Показать еще', callback_data='next'),
			InlineKeyboardButton(text = 'Назад', callback_data='back')
		]
		])






from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from func import lang_bot
import json

mas={}
menu_catalog=[]
menu_category=[]

def catalog(user_id,lang):
	#Создание списка состояний
	global mas
	if user_id in mas.keys():
		user=mas[user_id]
		user['lang']=lang
	else:
		mas[user_id]={}
		add=mas[user_id]
		add['lang']=lang		
		#print(mas)
	menu=[]	
	book=lang_bot(lang)
	for v in book:
		if v in menu_catalog:
			l=''	
		else:
			menu_catalog.append(v)
		strok=KeyboardButton(text=v)
		menu.append(strok)
	d=menu
	stok=len(d)//2
	ost=len(d)%2
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
	
	catalog_menu = ReplyKeyboardMarkup(keyboard=masiv, resize_keyboard=True)
	return catalog_menu

def category(user_id,catal):
	menu=[]
	book=''
	global mas
	user=mas[user_id]
	lang=user['lang']
	if lang=='Русский язык':
		with open('files/ricamare_ru.json', 'r', encoding='utf-8') as f:
			book=json.load(f)
	elif lang=='Українська мова':
		with open('files/ricamare_ua.json', 'r', encoding='utf-8') as f:
			book=json.load(f)
	
	for cat in book[catal]:
		if cat in menu_category:
			l=''	
		else:
			menu_category.append(cat)
		strok=KeyboardButton(text=cat)
		menu.append(strok)	
	d=menu
	stok=len(d)//2
	ost=len(d)%2
	mass=[]
	if stok>0:
		for i in range(stok):
			if i==0:
				mass.append([d[i],d[i+1]])
			elif i>0:
				mass.append([d[2*i],d[2*i+1]])
		if ost>0:
			if ost==1:
				mass.append([d[2*(i+1)]])       
	elif stok==0:
		if ost>0:
			if ost==1:
				mass.append([d[0]])
	if lang=='Русский язык':
		mass.append(['Главное меню'])
	elif lang=='Українська мова':
		mass.append(['Головне меню'])	
	catalog_menu = ReplyKeyboardMarkup(keyboard=mass, resize_keyboard=True)
	return catalog_menu


def back_menu(user_id):
	global mas
	menu=[]
	user=mas[user_id]
	lang=user['lang']
	if lang=='Русский язык':
		spisok=['Назад','Показать еще','Обратный звонок']
		for cat in spisok:
			strok=KeyboardButton(text=cat)
			menu.append(strok)
	elif lang=='Українська мова':
		spisok=['Назад','Показати ще','Обратний дзвінок']
		for cat in spisok:
			strok=KeyboardButton(text=cat)
			menu.append(strok)
	
	strok=KeyboardButton(text=spisok[2],request_contact=True)
	menu[2]=strok
	d=menu
	stok=len(d)//2
	ost=len(d)%2
	masss=[]
	if stok>0:
		for i in range(stok):
			if i==0:
				masss.append([d[i],d[i+1]])
			elif i>0:
				masss.append([d[2*i],d[2*i+1]])
		if ost>0:
			if ost==1:
				masss.append([d[2*(i+1)]])       
	elif stok==0:
		if ost>0:
			if ost==1:
				masss.append([d[0]])
	
	menu_back = ReplyKeyboardMarkup(keyboard=masss,resize_keyboard=True)
	return menu_back



def menu_end(lang):
	menu=[]
	if lang=='Русский язык':
		spisok=['🛒 Корзина','Главное меню','✅ Подтвердить заказ']
		for cat in spisok:
			strok=KeyboardButton(text=cat)
			menu.append(strok)
	elif lang=='Українська мова':
		spisok=['🛒 Кошик','Головне меню','✅ Підтвердити замовлення']
		for cat in spisok:
			strok=KeyboardButton(text=cat)
			menu.append(strok)
	
	strok=KeyboardButton(text=spisok[2],request_contact=True)
	menu[2]=strok
	d=menu
	stok=len(d)//2
	ost=len(d)%2
	masss=[]
	if stok>0:
		for i in range(stok):
			if i==0:
				masss.append([d[i],d[i+1]])
			elif i>0:
				masss.append([d[2*i],d[2*i+1]])
		if ost>0:
			if ost==1:
				masss.append([d[2*(i+1)]])       
	elif stok==0:
		if ost>0:
			if ost==1:
				masss.append([d[0]])
	
	menu_back = ReplyKeyboardMarkup(keyboard=masss,resize_keyboard=True)
	return menu_back





def menu_main(user_id):
	global mas
	try:
		user=mas[user_id]
		lang=user['lang']
		menu=catalog(user_id,lang)
	except Exception:
		menu==None
	return menu
	


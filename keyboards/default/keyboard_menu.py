from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu_main(lang):
	bot=['Главное меню','Головне меню']
	text=''
	if lang=='Українська мова':
		text=bot[1]
	else:
		text=bot[0]
	kb_menu_b = ReplyKeyboardMarkup(
		keyboard=[
			[
				KeyboardButton(text=text)
			]
	],resize_keyboard=True)
	return kb_menu_b



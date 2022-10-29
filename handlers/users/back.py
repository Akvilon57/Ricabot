from aiogram import types  
from loader import dp, bot
from func import lang_bot, zakaz_list, basket
from aiogram.utils.markdown import hbold, hcode, hlink
from keyboards.category import menu_catalog, category, mas
from aiogram.types import Message, CallbackQuery
from keyboards.inline import menu_iline, menu_iline2, menu_basket_eror, menu_del, basket_del_menu
from keyboards.category import menu_end
from utils.misc import rate_limit


@rate_limit(limit=5)

@dp.callback_query_handler()
async def  chat_privat(call: CallbackQuery):
	#await call.answer(cache_time = 60)
	#------------------ Назад ---------------------
	if call.data == 'back':
		await call.answer(cache_time = 60)
		user = mas[call.from_user.id]
		last_catalog=user['last_catalog']
		await call.message.answer(f'➡ {last_catalog}', reply_markup=category(call.from_user.id,last_catalog))
	#------------------ Следующий товар ---------------------
	if call.data == 'next':
		await call.answer(cache_time = 60)
		user=mas[call.from_user.id]
		categ=user['last_category']
		lang=user['lang']
		catalog=user['last_catalog']
		#print(mas)

		slova = ['Цена: ','Полная цена: ','Акционная цена🔥: ','Состав: ']
		predl = 'Вы, просмотрели весь товар из этой категории. Можите выбрать другую.'
		if lang=='Українська мова':
			slova=['Ціна: ','Повна ціна: ','Акційна ціна🔥: ','Склад: ']
			predl = 'Ви переглянули весь товар з цієї категорії. Можна вибрати іншу.'
		
		infa=lang_bot(lang)
		categorys=infa[catalog]
		carts=categorys[categ]
		cart_dlin=len(carts)

		st=''
		st_catalog=0
		st_categor=0
		for inf in infa:
			if inf==catalog:
				for catt in categorys:
					if catt==categ:
						st=st_catalog
						#print(catt,st)
						#print(inf,st_categor)
						break
					else:
						st_categor+=1
			else:
				st_catalog+=1

		#print(cart_dlin)
		if cart_dlin > user['numb_category']:
	
			numb_cart=user['numb_category']
			k=carts[numb_cart]
			cart=''
			
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
			
			await bot.send_photo(call.from_user.id, photo=foto[0], caption=cart, reply_markup=menu_iline(lang,st,st_categor,numb_cart))

	#---------------------------------------------
			user['numb_category'] +=1
		
		else: 
			await call.message.answer(predl,reply_markup=category(call.from_user.id,catalog))
			
	




	else:
		if 'col' in call.data:
			await call.answer(cache_time = 60)
			tovar=call.data.split()
			#print(tovar)

			user=mas[call.from_user.id]
			lang=user['lang']
			infa=lang_bot(lang)

			slowar='Выберете размер и цвет:'
			if lang=='Українська мова':
				slowar='Виберіть розмір та колір'
	
			infa_cart=call.data.replace('col','buy')
			#print(infa_cart)
			#print(call.data)
			price=''
			articuls=''
			categ=''
			catalog=''
			foto=''
			size=''
			s=-1
			k=-1
			for i in infa:
				s+=1
				if s==int(tovar[1]):
					catalog=i
					categorys=infa[catalog]
					for c in categorys:
						k+=1
						if k==int(tovar[2]):
							categ=c
							carts=categorys[categ]
							don=int(tovar[3])
							cart=carts[don]
							size=cart['size']
							foto=cart['foto']
							articuls=cart['articul']
							price=''.join(cart['price_new'].split())
							dlin=len(foto)
							if dlin>1:	
								media = types.MediaGroup()
								sdlin=0
								for fotos in foto:
									if sdlin==0:
										media.attach_photo(fotos)
										sdlin+=1
									else:
										media.attach_photo(fotos)
								await bot.send_media_group(call.from_user.id, media=media)

							await call.message.answer(f'{hbold(slowar)}',reply_markup=menu_iline2(lang,infa_cart,size,price,articuls))
							
							break

		elif 'buy' in call.data:
			tovar=call.data.split()
			user_id=mas[call.from_user.id]
			lang=user_id['lang']
			predl=['Ваша корзина переполнена. Очистите ее или свяжитесь с менеджером','Товар добавлен в корзину:\n_____________________________\n\n','Артикул: ','\nРазмер: ','\nЦена: ']
			if lang=='Українська мова':
				predl=["Ваш кошик переповнений. Очистить його або зв'яжіться з менеджером",'Товар доданий до кошика:\n____________________________\n\n','Артикул: ','\nРозмір: ','\nЦіна: ']
			user=str(call.from_user.id)
			if zakaz_list(user, tovar[5], tovar[6], tovar[4], 'w'):
				await call.message.answer(predl[0],reply_markup=menu_basket_eror(lang))
				
			else:
				await call.message.answer(f'{hbold(predl[1])}{predl[2]}{tovar[5]}{predl[3]}{tovar[6].title()}{predl[4]}{tovar[4]}',reply_markup=menu_del(lang,tovar[5],tovar[6],tovar[4]))           
					


		elif 'clear' in call.data:
			user_id=mas[call.from_user.id]
			lang=user_id['lang']
			user=str(call.from_user.id)
			zakaz_list(user,'1','1','1')
			if lang=='Русский язык':	
				await bot.answer_callback_query(callback_query_id=call.id,text=f'Ваша корзина успешно очищена\nМожите продолжить покупки',show_alert=True)
			elif lang=='Українська мова':
				await bot.answer_callback_query(callback_query_id=call.id,text=f'Ваш кошик успішно очищений\nМожна продовжити покупки',show_alert=True)


		elif 'del' in call.data:
			tovar=call.data.split()
			user_id=mas[call.from_user.id]
			lang=user_id['lang']
			slov_del=[' уже был удален из вашей корзины.','Товар успешно удален с корзины:\n','\n\nАртикул: ','\nРазмер:	']
			if lang =='Українська мова':
				slov_del=[' вже був видалений з вашого кошика.','Товар успішно видалено з кошика:\n','\n\nАртикул: ','\nРозмір:	']
			user=str(call.from_user.id)
			if zakaz_list(user, tovar[1], tovar[2], tovar[3], 'del'):
				await bot.answer_callback_query(callback_query_id=call.id,text=f'Артикул {tovar[1]}{slov_del[0]}\n',show_alert=True)
			else:
				stro='_'*40
				await bot.answer_callback_query(callback_query_id=call.id,text=f'{slov_del[1]}{stro}{slov_del[2]}{tovar[1]}{slov_del[3]}{tovar[2].title()}',show_alert=True)
				

		elif 'basket' in call.data:
			user_id=mas[call.from_user.id]
			lang=user_id['lang']
			user=str(call.from_user.id)
			bask=basket(lang, user,'read')
			if bask:
				bas=" ".join(bask)
				await call.message.answer(f'{bas}', reply_markup=basket_del_menu(lang, user))
			else:
				if lang=='Русский язык': 
					await bot.answer_callback_query(callback_query_id=call.id,text=f'Здесь пока пусто 🤔\nОткройте меня позже.',show_alert=True)
				elif lang=='Українська мова':
					await bot.answer_callback_query(callback_query_id=call.id,text=f'Тут поки пусто 🤔\nВідкрийте мене пізніше.',show_alert=True)


		elif 'ok' in call.data:
			user_id=mas[call.from_user.id]
			lang=user_id['lang']
			user=str(call.from_user.id)
			bask=basket(lang, user,'read')
			if bask:
				bas=" ".join(bask)
				await call.message.answer(f'{bas}', reply_markup=menu_end(lang))
			else:
				if lang=='Русский язык': 
					await bot.answer_callback_query(callback_query_id=call.id,text=f'Здесь пока пусто 🤔\nОткройте меня позже.',show_alert=True)
				elif lang=='Українська мова':
					await bot.answer_callback_query(callback_query_id=call.id,text=f'Тут поки пусто 🤔\nВідкрийте мене пізніше.',show_alert=True)


		elif 'zak' in call.data:
			from data.config import JZAK
			import json
			with open(JZAK, 'r',encoding='utf-8') as fi:
				datas = json.load(fi)
				s=''
				if len(datas)==0:
					s='Заказов нет'
				else:
					for key,value in datas.items():
						s=str(value)
						s = s.replace('[', '')
						s = s.replace(']', '')
						s = s.replace(',', '')
						s = s.replace("'", '')
				await call.message.answer(f'{s}')
				fi.close()

		elif 'user' in call.data:
			from data.config import JRASS, JBASK
			import json
			dl=''
			dlin=''
			basklin=''
			with open(JRASS, 'r',encoding='utf-8') as fi:
				datas = json.load(fi)
				if 'users' in datas:
					s=datas["users"]
					dlin=len(s)
				else:
					dlin=0	
				if 'del_basket' in datas:
					d=datas['del_basket']
					dl=len(d)
				else:
					dl=0
				fi.close()
			with open(JBASK, 'r',encoding='utf-8') as file:
				data = json.load(file)
				basklin=len(data)
				file.close()
			
			await call.message.answer(f'Количество зашедших пользователей: {dlin} человек\nКоличество корзин:{basklin}\nКоличество удаленных кoрзин: {dl}шт.')
				


		elif 'jsc' in call.data:
			from data.config import JRASS, JZAK
			import json
			with open(JRASS, 'r+',encoding='utf-8') as fi:
				datas = json.load(fi)
				datas={}
				fi.seek(0)
				fi.truncate(0)
				json.dump(datas, fi)
				fi.close()
			with open(JZAK, 'r+',encoding='utf-8') as file:
				datas = json.load(file)
				datas={}
				file.seek(0)
				file.truncate(0)
				json.dump(datas, file)
				file.close()
			await call.message.answer(f'Статистика очищина')

		



			





			




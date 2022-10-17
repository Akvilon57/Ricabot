from aiogram import types  
from loader import dp,bot
import asyncio


async def ok(dp):
	print('ok')
	
	await bot.send_message(1962555564,'Все ок')
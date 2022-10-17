from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#Создаем переменную бота 
bot = Bot(token = config.BOT_TOKEN, parse_mode= types.ParseMode.HTML)
#Создаем диспечер

dp = Dispatcher(bot,storage=MemoryStorage())


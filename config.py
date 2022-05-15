from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BRON_CHANNEL = "-1001774409771"
token = '5286546614:AAEGjGi5elS1quZcfopurzE2-gYPYisubf4'
storage = MemoryStorage()
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


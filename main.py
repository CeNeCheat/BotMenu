import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from random import randint
from handlers import client

API_TOKEN = '5370162416:AAGulsDg5LFCe5eWtXUxpbBsNirf9xZIp74'

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage=storage)


client.register_handlers(dp)        
if __name__  == "__main__":
    executor.start_polling(dp, skip_updates=True)
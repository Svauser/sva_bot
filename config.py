from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL + "http://proxy.server:3128"
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN, proxy=PROXY_URL)
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
GROUP_ID = config("GROUP_ID")
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
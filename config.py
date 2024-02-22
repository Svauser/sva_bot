from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)

MEDIA_DESTINATION = config("MEDIA_DESTINATION")
GROUP_ID = config("GROUP_ID")
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)
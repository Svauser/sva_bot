import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
from keyboards import start_inline_buttons,registration_keyboard
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac_sign = State()
    job = State()
    gender = State()
    photo = State()
async def registration_start(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("Ваш никнейм?")
    await RegistrationStates.nickname.set()
async def load_nickname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
    await message.answer('Напишите немного о себе')
    await RegistrationStates.next()
async def load_biography(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
    await message.answer("Ваш возраст?(Используйте цифры)")
    await RegistrationStates.next()
async def load_age(message: types.Message,
                   state: FSMContext):
  age=message.text
  if age.isdigit():
      if int(age)<12:
          await message.answer('Возрастное ограничение 18+')
      else:
          async with state.proxy() as data:
              data['age'] = int(message.text)
          await message.answer("Ваш знак зодиака?")
          await RegistrationStates.next()
  else:
      await message.answer("Используйте только числа")

async def load_zodiac_sign(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['zodiac_sign'] = message.text
    await message.answer('Где вы работаете?')
    await RegistrationStates.next()

async def load_job(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['job'] = message.text
    await message.answer('Ваш гендер ?',reply_markup= await registration_keyboard.gender_keyboard())
    await RegistrationStates.next()
async def load_gender(message: types.Message,state: FSMContext):
    gender= message.text
    if not gender in ['Мужчина','Женщина','????']:
        await message.answer('Выберите из списка!')
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
        await message.answer('Отправьте ваше фото')
        await RegistrationStates.next()
async def load_photo(message: types.Message,
                     state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            biography=data['biography'],
            age=data['age'],
            zodiac_sign=data['zodiac_sign'],
            job= data['job'],
            gender=data['gender'],
            photo=path.name
        )
        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    biography=data['biography'],
                    age=data['age'],
                    zodiac_sign=data['zodiac_sign'],
                    job=data['job'],
                    gender=data['gender']
                )
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Регистрация прошла успешно!"
        )
        await state.finish()
def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegistrationStates.zodiac_sign,
        content_types=['text']
    )
    dp.register_message_handler(
        load_job,
        state=RegistrationStates.job,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
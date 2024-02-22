from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

async def gender_keyboard():
    markup=ReplyKeyboardMarkup()
    male=KeyboardButton('Мужчина')
    female= KeyboardButton('Женщина')
    undefind=KeyboardButton('????')
    markup.add(male,female,undefind)
    return markup

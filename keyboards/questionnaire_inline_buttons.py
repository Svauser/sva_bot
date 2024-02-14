from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    marvel_button = InlineKeyboardButton(
        "Marvel",
        callback_data="Marvel"
    )
    dc_button = InlineKeyboardButton(
        "Dc",
        callback_data="Dc"
    )
    markup.add(marvel_button)
    markup.add(dc_button)
    return markup
async def marvel_keyboard():
    markup=InlineKeyboardMarkup()
    x_man_button = InlineKeyboardButton(
        "X-man",
        callback_data="X-man"
    )
    avangers_button = InlineKeyboardButton(
        "Avangers",
        callback_data="Avangers"
    )
    markup.add(x_man_button)
    markup.add(avangers_button)
    return markup


async def dc_keyboard():
    markup=InlineKeyboardMarkup()
    suicidesquad_button = InlineKeyboardButton(
        "Suicide squad",
        callback_data="Suicide squad"
    )
    justiceleague_button = InlineKeyboardButton(
        "Justice league",
        callback_data="Justice league"
    )
    markup.add(suicidesquad_button)
    markup.add(justiceleague_button)
    return markup


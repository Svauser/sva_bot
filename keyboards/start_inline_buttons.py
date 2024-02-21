from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Опросник",
        callback_data="start_questionnaire"
    )
    check_ban_button= InlineKeyboardButton(
        "Проверить статус",
        callback_data="check_ban"
    )
    markup.add(questionnaire_button)
    markup.add(check_ban_button)
    return markup
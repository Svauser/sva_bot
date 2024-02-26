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
    registration_button=InlineKeyboardButton(
        "Регистрация",
        callback_data='registration'
    )
    my_profile_button = InlineKeyboardButton(
        "Мой профиль ",
        callback_data="my_profile"
    )
    profiles_button = InlineKeyboardButton(
        "Смотреть другие профили",
        callback_data="random_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Reference Menu ",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button)
    markup.add(check_ban_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(profiles_button)
    markup.add(reference_button)
    return markup
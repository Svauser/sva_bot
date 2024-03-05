import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot
from database import bot_db
from keyboards.reference_inline_buttons import (
    reference_menu_keyboard,
)
import const
import os
import binascii


async def reference_menu_call(call: types.CallbackQuery):
    db = bot_db.Database()
    result = db.sql_reference_menu_info(
        tg_id=call.from_user.id
    )
    print(result)
    await bot.send_message(
            chat_id=call.from_user.id,
            text=const.REFERENCE_MENU_TEXT.format(
                balance=result['balance'],
                count=result['count'],
            ),
            reply_markup=await reference_menu_keyboard()
        )


async def reference_link_call(call: types.CallbackQuery):
    db = bot_db.Database()
    user = db.sql_select_user(
        tg_id=call.from_user.id
    )
    if not user['link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        db.sql_update_reference_link(
            link=link,
            tg_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ваша новая ссылка: {link}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Ваша ссылка: {user['link']}"
        )

async def reference_list_call(call: types.CallbackQuery):
    db = bot_db.Database()
    referrals = db.sql_get_referrals(call.from_user.id)
    if referrals:
        message_text = "Ваши реферралы:\n"
        for referral in referrals:
            message_text += f"{referral['referral_telegram_id']}\n"
    else:
        message_text = "У вас нет реферралов."
    await bot.send_message(
        chat_id=call.from_user.id,
        text=message_text
    )

def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == "reference_menu"
    )
    dp.register_callback_query_handler(
        reference_link_call,
        lambda call: call.data == "reference_link"
    )
    dp.register_callback_query_handler(
        reference_list_call,
        lambda call: call.data == "reference_list"
    )

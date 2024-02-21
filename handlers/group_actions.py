import datetime
from aiogram import types, Dispatcher
from database import bot_db
from config import bot, GROUP_ID
from profanity_check import predict, predict_prob



async def group_observation(message: types.Message):
    db = bot_db.Database()
    bad_words_prob=predict_prob([message.text])
    if bad_words_prob > 0.8:
        if not db.sql_select_ban_user(message.from_user.id):
            db.sql_insert_ban_user(message.from_user.id)
            await message.answer(f'{message.from_user.first_name},\n'
                                 f'без мата')
            await bot.delete_message(message.chat.id,message.message_id)
        elif db.sql_select_ban_user(message.from_user.id)['count']>=3:
            await bot.kick_chat_member(message.chat.id,message.from_user.id)
            await bot.send_message(message.from_user.id,text="Вас удалили из группы за мат")

        else:
            db.sql_update_ban_count(message.from_user.id)
            await message.answer(f'{message.from_user.first_name},\n'
                                 f'вторичное нарушение')
            await bot.delete_message(message.chat.id, message.message_id)
async def check_ban(call:types.CallbackQuery):
    db= bot_db.Database()
    user=db.sql_select_ban_user(call.from_user.id)
    if not user:
        text=f'Все ок'
        await call.message.answer(text)
    else:
        text=f"У вас нарушений - **{user['count']}**"
        await call.message.answer(text)
def register_group_actions_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(check_ban,
                                       lambda call: call.data =='check_ban')
    dp.register_message_handler(
        group_observation
    )
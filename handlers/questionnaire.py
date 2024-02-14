from aiogram import types, Dispatcher
from config import bot
from keyboards import questionnaire_inline_buttons


async def questionnaire_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=" Marvel or Dc?",
        reply_markup=await questionnaire_inline_buttons.questionnaire_keyboard()
    )


async def marvel_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Круто!\n"
             "X-man or Avangers ?",
        reply_markup=await questionnaire_inline_buttons.marvel_keyboard()

    )

async def dc_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Круто\n"
             "Suicide squad or Justice league ?",
        reply_markup=await questionnaire_inline_buttons.dc_keyboard()
    )


async def x_man_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Snikt!"
    )


async def avangers_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Assamble!"
    )
async def suicidesquad_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Puddin!"
    )
async def justiceleague_answer(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Marta!"
    )
def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start,
        lambda call: call.data == "start_questionnaire"
    )
    dp.register_callback_query_handler(
        marvel_answer,
        lambda call: call.data == "Marvel"
    )
    dp.register_callback_query_handler(
        dc_answer,
        lambda call: call.data == "Dc"
    )
    dp.register_callback_query_handler(
        x_man_answer,
        lambda call: call.data == "X-man"
    )
    dp.register_callback_query_handler(
        avangers_answer,
        lambda call: call.data == "Avangers"
    )
    dp.register_callback_query_handler(
        suicidesquad_answer,
        lambda call: call.data == "Suicide squad"
    )
    dp.register_callback_query_handler(
        justiceleague_answer,
        lambda call: call.data == "Justice league"
    )
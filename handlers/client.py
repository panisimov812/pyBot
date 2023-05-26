from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)  # ответ пишем в лс
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \nhttps://t.me/zarplataokbot')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'C 10 до 18 каждый день')


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Чехова 12')


@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])

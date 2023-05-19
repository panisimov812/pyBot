from aiogram import types, Dispatcher
from create_bot import dp, bot


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')  # ответ пишем в лс
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему \nhttps://t.me/zarplataokbot')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'C 10 до 18 каждый день')


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Чехова 12')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['расположение'])

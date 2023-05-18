from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')


# ***=========клиентская часть***
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет')  # ответ пишем в лс
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему https://t.me/zarplataokbot')


@dp.message_handler(commands=['Режим_работы'])
async def shop_open_houers(message: types.Message):
    await bot.send_message(message.from_id, 'C 10 до 18')


@dp.message_handler(commands=['Зарплаты'])
async def salary(message: types.Message):
    await message.reply('2323')

@dp.message_handler()
async def echo_bot(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

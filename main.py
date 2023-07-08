import logging

from aiogram import Bot, Dispatcher, executor, types

import inline_keyboard
import messages
import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands = "weather")
async def show_weather(message: types.Message):
    await message.answer(text = messages.weather())

@dp.message_handler(commands = ["start", "help"])
async def show_help_message(message: types.Message):
    await message.answer(text = f"This bot can gat current weather from your IP address.\n/weather - weather temperature, humidity\n/wind - give information about wind\n/sun_time - give information about sunrise and sunset")

@dp.message_handler(commands = "wind")
async def show_wind(message: types.Message):
    await message.answer(text = messages.wind())

@dp.message_handler(commands = "sun_time")
async def show_sun_time(message: types.Message):
    await message.answer(text = messages.sun_time())

@dp.message_handler(text = "weather")
async def process_callback_weather(callback_query: types.callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text = message.weather())

@dp.message_handler(text = "wind")
async def process_callback_wind(callback_query: types.callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text = message.wind())

@dp.message_handler(text = "sun_time")
async def process_callback_wind(callback_query: types.callback_query):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, text = message.sun_time())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

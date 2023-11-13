import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InputFile 
from Table import s, day_week, day_in
from config import TOKEN
from datetime import date

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")
    key_board = ReplyKeyboardBuilder()

    for i in range(6, -1, -1):
        key_board.add(types.KeyboardButton(text=day_in[i]))

    key_board.adjust(3)

    await message.answer('Выберите день недели:', reply_markup=key_board.as_markup(resize_keyboard=True))


@dp.message(Command("table"))
async def cmd_table(message: types.Message):
    week_day = date.today().weekday() + 1

    tbl = ''

    tbl += 'Сегодня ' + s[week_day][0] + ':\n'

    for i in range(1, len(s[week_day])):
        tbl += s[week_day][i]
        tbl += '\n'

    await message.answer(tbl)


@dp.message(Command('gdz'))
async def cmd_rand(message: types.Message):
    key_board = InlineKeyboardBuilder()

    key_board.row(types.InlineKeyboardButton(text = 'Euroki', url = 'https://www.euroki.org/gdz/ru/algebra/10_klass/reshebnik-po-algebre-10-klass-nikolskii-potapov-217'))
    key_board.row(types.InlineKeyboardButton(text = 'GDZ', url = 'https://gdz.ru/class-10/algebra/nikolskij-potapov/'))
    key_board.row(types.InlineKeyboardButton(text = 'Megareshaba', url = "https://megaresheba.ru/publ/reshebnik/algebra/reshebnik_po_algebre_10_klass_nikolskij_potapov"))
    key_board.row(types.InlineKeyboardButton(text = 'Reshak', url = "https://reshak.ru/reshebniki/algebra/10/nikol/index.html"))
    
    key_board.adjust(2)

    await message.answer('Выберите ГДЗ', reply_markup=key_board.as_markup(),)


@dp.message(Command('all_tables'))
async def cmd_rand(message: types.Message):
    await message.answer('Эта функция, к сожелению ещё в разработке!')


@dp.message(Command('rand'))
async def cmd_rand(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(lambda msg: msg.text in day_in)
async def cmd_table(message: types.Message):
    week_day = day_week[message.text]

    tbl = ''

    tbl += 'Расписание в день ' + s[week_day][0] + ':\n'

    for i in range(1, len(s[week_day])):
        tbl += s[week_day][i]
        tbl += '\n'

    await message.answer(tbl)


@dp.message(F.text)
async def cmd_table(message: types.Message):
    await message.reply('Я вас не понял!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from BD import checker, reporter, debtor_creator, debtor_forgiver, machine_checker, time_teller, m_n_computer
from time_conversion import white, fast_st, dry
from aiogram import types, Dispatcher, Bot
from datetime import datetime
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = open("tk.txt", 'r').readline()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def timer():
    while True:
        await asyncio.sleep(20)
        q = checker()
        mp = InlineKeyboardMarkup()
        mp.add(InlineKeyboardButton("Я забрал(-а) все вещи из прачечной", callback_data="but_fin"))
        if q != 0:
            debtor_creator(q[0][0], q[1][0])
            await bot.send_message(q[0][0], 'Заберите вещи из прачечной', reply_markup=mp)


@dp.callback_query_handler(lambda c: c.data == "but_fin")
async def button_reaction(call: types.callback_query):
    debtor_forgiver(call.message.chat.id)
    await bot.send_message(call.message.chat.id, "Молодец!")


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1f = InlineKeyboardButton("На 1-ом", callback_data="but_1f")
    but_2f = InlineKeyboardButton("На 2-ом", callback_data="but_2f")
    but_3f = InlineKeyboardButton("На 3-ем", callback_data="but_3f")
    markup.add(but_1f, but_2f, but_3f)

    await bot.send_message(message.chat.id,
                           f'{message.from_user.username.capitalize()}, вас приветствует бот, предназначеный для удобного использования прачечной.'
                           f'На каком этаже вы собираетесь пользоваться прачечной?', reply_markup=markup)


# первый этаж
@dp.callback_query_handler(lambda c: c.data == "but_1f")
async def button_reaction(call: types.callback_query):
    markup1f = InlineKeyboardMarkup()

    but_1f1m = InlineKeyboardButton("Стиральной машинкой", callback_data="but_1f1m")
    but_1f2m = InlineKeyboardButton("Сушильной машинкой", callback_data="but_1f2m")

    markup1f.add(but_1f1m, but_1f2m)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Чем вы хотите воспользоваться?",
                           reply_markup=markup1f)


@dp.callback_query_handler(lambda c: c.data == "but_1f1m")
async def button_reaction(call: types.callback_query):
    markup1f1m = InlineKeyboardMarkup()

    but_1f1m1r = InlineKeyboardButton("Белое/Цветное", callback_data="but_1f1m1r")
    but_1f1m2r = InlineKeyboardButton("Быстрая", callback_data="but_1f1m2r")
    markup1f1m.add(but_1f1m1r, but_1f1m2r)
    await bot.send_message(call.message.chat.id, "Выберите режим", reply_markup=markup1f1m)


@dp.callback_query_handler(lambda c: c.data == "but_1f1m1r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    white(call.message.chat.id, m_n_computer(1), t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_1f1m2r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    fast_st(call.message.chat.id, m_n_computer(1), t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_1f2m")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    dry(call.message.chat.id, 13, t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда сушка будет окончена")


# второй этаж
@dp.callback_query_handler(lambda c: c.data == "but_2f")  # реакция на нажатие кнопки
async def button_reaction(call: types.callback_query):
    markup2f = InlineKeyboardMarkup()

    but_2f1m = InlineKeyboardButton("Стиральной машинкой", callback_data="but_2f1m")
    but_2f2m = InlineKeyboardButton("Сушильной машинкой", callback_data="but_2f2m")

    markup2f.add(but_2f1m, but_2f2m)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Чем вы хотите воспользоваться?",
                           reply_markup=markup2f)


@dp.callback_query_handler(lambda c: c.data == "but_2f1m")  # реакция на нажатие кнопки
async def button_reaction(call: types.callback_query):
    markup2f1m = InlineKeyboardMarkup()

    but_2f1m1r = InlineKeyboardButton("Белое/Цветное", callback_data="but_2f1m1r")
    but_2f1m2r = InlineKeyboardButton("Быстрая", callback_data="but_2f1m2r")

    markup2f1m.add(but_2f1m1r, but_2f1m2r)

    await bot.send_message(call.message.chat.id, "Выберите режим", reply_markup=markup2f1m)


@dp.callback_query_handler(lambda c: c.data == "but_2f1m1r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    white(call.message.chat.id, m_n_computer(2), t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_2f1m2r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    fast_st(call.message.chat.id, m_n_computer(2), t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_2f2m")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    dry(call.message.chat.id, 23, t)
    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда сушка будет окончена")


# третий этаж
@dp.callback_query_handler(lambda c: c.data == "but_3f")  # реакция на нажатие кнопки
async def button_reaction(call: types.callback_query):
    markup3f = InlineKeyboardMarkup()

    but_3f1m = InlineKeyboardButton("Стиральной машинкой", callback_data="but_3f1m")
    but_3f2m = InlineKeyboardButton("Сушильной машинкой", callback_data="but_3f2m")

    markup3f.add(but_3f1m, but_3f2m)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Чем вы хотите воспользоваться?",
                           reply_markup=markup3f)


@dp.callback_query_handler(lambda c: c.data == "but_3f1m")  # реакция на нажатие кнопки
async def button_reaction(call: types.callback_query):
    markup3f1m = InlineKeyboardMarkup()

    but_3f1m1r = InlineKeyboardButton("Белое/Цветное", callback_data="but_3f1m1r")
    but_3f1m2r = InlineKeyboardButton("Быстрая", callback_data="but_3f1m2r")

    markup3f1m.add(but_3f1m1r, but_3f1m2r)

    await bot.send_message(call.message.chat.id, "Выберите режим", reply_markup=markup3f1m)


@dp.callback_query_handler(lambda c: c.data == "but_3f1m1r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    white(call.message.chat.id, m_n_computer(3), t)

    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_3f1m2r")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    fast_st(call.message.chat.id, m_n_computer(3), t)
    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда стирка будет окончена")


@dp.callback_query_handler(lambda c: c.data == "but_3f2m")
async def button_reaction(call: types.callback_query):
    t = [datetime.now().hour, datetime.now().minute]
    dry(call.message.chat.id, 33, t)
    await bot.send_message(call.message.chat.id, "Вы будете уведомлены, когда сушка будет окончена")


@dp.message_handler(commands=['report'])
async def begin(message: types.Message):
    markup_r = InlineKeyboardMarkup()
    but_1f_r = InlineKeyboardButton("На 1-ом", callback_data="but_1f_r")
    but_2f_r = InlineKeyboardButton("На 2-ом", callback_data="but_2f_r")
    but_3f_r = InlineKeyboardButton("На 3-ем", callback_data="but_3f_r")
    markup_r.add(but_1f_r, but_2f_r, but_3f_r)

    await bot.send_message(message.chat.id,
                           f'В прачечной какого этажа оставили вещи?', reply_markup=markup_r)


@dp.callback_query_handler(lambda c: c.data == "but_1f_r")
async def button_reaction(call: types.callback_query):
    zapros1 = reporter(1)
    if zapros1 != 0:
        for i in zapros1:
            mp1 = InlineKeyboardMarkup()
            mp1.add(InlineKeyboardButton("Я забрал(-а) все вещи из прачечной", callback_data="but_fin"))
            await bot.send_message(i, "Заберите, пожалуйста, вещи из прачечной", reply_markup=mp1)
            await bot.send_message(call.message.chat.id,
                                   f'Забывшему вещи было отправлено уведомление')
    else:
        await bot.send_message(call.message.chat.id,
                               f'Забывшему вещи было отправлено уведомление')


@dp.callback_query_handler(lambda c: c.data == "but_2f_r")
async def button_reaction(call: types.callback_query):
    zapros2 = reporter(2)
    if zapros2 != 0:
        for i in zapros2:
            mp2 = InlineKeyboardMarkup()
            mp2.add(InlineKeyboardButton("Я забрал(-а) все вещи из прачечной", callback_data="but_fin"))
            await bot.send_message(i, "Заберите, пожалуйста, вещи из прачечной", reply_markup=mp2)
            await bot.send_message(call.message.chat.id,
                                   f'Забывшему вещи было отправлено уведомление')
    else:
        await bot.send_message(call.message.chat.id,
                               f'Забывшему вещи было отправлено уведомление')


@dp.callback_query_handler(lambda c: c.data == "but_3f_r")
async def button_reaction(call: types.callback_query):
    zapros3 = reporter(3)
    if zapros3 != 0:
        for i in zapros3:
            mp3 = InlineKeyboardMarkup()
            mp3.add(InlineKeyboardButton("Я забрал(-а) все вещи из прачечной", callback_data="but_fin"))
            await bot.send_message(i, "Заберите, пожалуйста, вещи из прачечной", reply_markup=mp3)
            await bot.send_message(call.message.chat.id,
                                   f'Забывшему вещи было отправлено уведомление')
    else:
        await bot.send_message(call.message.chat.id,
                               f'Забывшему вещи было отправлено уведомление')


@dp.message_handler(commands=['check'])
async def begin(message: types.Message):
    markup_c = InlineKeyboardMarkup()
    but_1c = InlineKeyboardButton("На 1-ом", callback_data="but_1c")
    but_2c = InlineKeyboardButton("На 2-ом", callback_data="but_2c")
    but_3c = InlineKeyboardButton("На 3-ем", callback_data="but_3c")
    markup_c.add(but_1c, but_2c, but_3c)

    await bot.send_message(message.chat.id,
                           f' На каком этаже проверить количество свободных стиральных и сушильных машин?',
                           reply_markup=markup_c)


@dp.callback_query_handler(lambda c: c.data == "but_1c")
async def button_reaction(call: types.callback_query):
    r = machine_checker(1)
    spisok_mashinok1 = {11: "Свободна", 12: "Свободна", 13: "Свободна"}
    if r:
        for i in r:
            ttr = time_teller(i)
            for j in ttr:
                spisok_mashinok1[j[0]] = f"Освободится в {j[1]}:{j[2]}"
    await bot.send_message(call.message.chat.id,
                           f"Стиральная 1: {spisok_mashinok1[11]} \nСтиральная 2: {spisok_mashinok1[12]} \n"
                           f"Сушильная: {spisok_mashinok1[13]}")


@dp.callback_query_handler(lambda c: c.data == "but_2c")
async def button_reaction(call: types.callback_query):
    r = machine_checker(2)
    spisok_mashinok2 = {21: "Свободна", 22: "Свободна", 23: "Свободна"}
    if r:
        for i in r:
            ttr = time_teller(i)
            for j in ttr:
                spisok_mashinok2[j[0]] = f"Освободится в {j[1]}:{j[2]}"
    await bot.send_message(call.message.chat.id,
                           f"Стиральная 1: {spisok_mashinok2[21]} \nСтиральная 2: {spisok_mashinok2[22]} \n"
                           f"Сушильная: {spisok_mashinok2[23]}")


@dp.callback_query_handler(lambda c: c.data == "but_3c")
async def button_reaction(call: types.callback_query):
    r = machine_checker(3)
    spisok_mashinok = {31: "Свободна", 32: "Свободна", 33: "Свободна"}
    if r:
        for i in r:
            ttr = time_teller(i)
            for j in ttr:
                spisok_mashinok[j[0]] = f"Освободится в {j[1]}:{j[2]}"
    await bot.send_message(call.message.chat.id,
                           f"Стиральная 1: {spisok_mashinok[31]} \nСтиральная 2: {spisok_mashinok[32]} \n"
                           f"Сушильная: {spisok_mashinok[33]}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.create_task(dp.start_polling())
    loop.create_task(timer())
    loop.run_forever()

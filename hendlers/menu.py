from config import dp
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from app import btnMenu, btnbar, btnTime, btnBrn
btnkitchen = "馃嵄 啸袨袥袨袛袧蝎袝 袠 袚袨袪携效袠袝 袟袗袣校小袣袠"
btndes = "馃嵁 袛袝小袝袪孝蝎"
btnbzn = "馃 小袗袥袗孝蝎"
btnsup = "馃嵅 小校袩蝎"
btnkids = "馃懚 袛袝孝小袣袨袝 袦袝袧挟"
btngor = "馃 袚袨袪携效袠袝 袘袥挟袛袗"
btngril = "馃ォ GRILL-小孝袝袡袣袠"
btnsous = "馃嵔 小袨校小袗 袠 袚袗袪袧袠袪蝎"
btnnaz = "馃敊 袧袗袟袗袛"


@dp.message_handler(text=btnMenu)
async def cmd_menu(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("袙蝎袘袝袪袠孝袝 袪袗袟袛袝袥", reply_markup=markup)


@dp.message_handler(text=btnkitchen)
async def btn_kitchen(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/Menyu-04-20-2", reply_markup=markup)


@dp.message_handler(text=btnbzn)
async def btn_bzn(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/Menyu-04-20-3", reply_markup=markup)


@dp.message_handler(text=btngril)
async def btn_gril(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-4", reply_markup=markup)


@dp.message_handler(text=btngor)
async def btn_gor(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-5", reply_markup=markup)


@dp.message_handler(text=btnsup)
async def btn_sup(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-6", reply_markup=markup)


@dp.message_handler(text=btnkids)
async def btn_kids(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-7", reply_markup=markup)


@dp.message_handler(text=btnsous)
async def btn_sous(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-8", reply_markup=markup)


@dp.message_handler(text=btndes)
async def btn_des(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("https://telegra.ph/MENYU-04-20-9", reply_markup=markup)


@dp.message_handler(text=btnnaz)
async def btn_naz(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnMenu, btnbar, btnTime).add(btnBrn)
    await message.answer("袩袝袪袝啸袨袛 袧袗 袚袥袗袙袧袨袝 袦袝袧挟", reply_markup=markup)
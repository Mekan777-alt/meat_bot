from config import dp
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from app import btnMenu, btnbar, btnTime, btnBrn
btnkitchen = "🍱 ХОЛОДНЫЕ И ГОРЯЧИЕ ЗАКУСКИ"
btndes = "🍮 ДЕСЕРТЫ"
btnbzn = "🥗 САЛАТЫ"
btnsup = "🍲 СУПЫ"
btnkids = "👶 ДЕТСКОЕ МЕНЮ"
btngor = "🥙 ГОРЯЧИЕ БЛЮДА"
btngril = "🥩 GRILL-СТЕЙКИ"
btnsous = "🍽 СОУСА И ГАРНИРЫ"
btnnaz = "🔙 НАЗАД"


@dp.message_handler(text=btnMenu)
async def cmd_menu(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btnkitchen, btnbzn, btngril).add(btngor, btnsup, btnkids).add(btnsous, btndes, btnnaz)
    await message.answer("ВЫБЕРИТЕ РАЗДЕЛ", reply_markup=markup)


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
    await message.answer("ПЕРЕХОД НА ГЛАВНОЕ МЕНЮ", reply_markup=markup)
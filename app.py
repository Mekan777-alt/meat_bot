from config import dp
from aiogram import executor
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
import hendlers

btnMenu = "📖 МЕНЮ"
btnBrn = "📞 ЗАБРОНИРОВАТЬ"
btnTime = "🕗 РЕЖИМ РАБОТЫ"
btnbar = "🍾 БАР"


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btnMenu, btnbar, btnTime).add(btnBrn)
    await message.answer('ДОБРО ПОЖАЛОВАТЬ, {0.first_name}\n'
                         'Я Ваш личный бот, помощник.\n'
                         'Я помогу Вам ознакомиться с меню, режимом работы ресторана и '
                         'забронировать стол.'.format(
        message.from_user), reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
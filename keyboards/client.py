from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_menu = KeyboardButton('Меню')
button_order = KeyboardButton('Сделать заказ')
button_phones= KeyboardButton('Телефоны для справки')
button_review = KeyboardButton('Оставить отзыв')
button_showrev = KeyboardButton('Посмотреть отзывы')
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_menu).add(button_order).row(button_review, button_showrev).add(button_phones)

button_hot=KeyboardButton('Горячие блюда')
button_drink=KeyboardButton('Напитки')
button_snaks=KeyboardButton('Закуски')
button_desert =KeyboardButton('Десерты')
button_cancel = KeyboardButton('Отмена')
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
button_cancel2 = KeyboardButton('Отмена')
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(button_hot).add(button_snaks).add(button_drink).add(button_desert).add(button_cancel2)

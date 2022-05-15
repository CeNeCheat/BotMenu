from keyboards import kb_menu
from keyboards import kb_main
from keyboards import kb_cancel
import sqlite3
import review as re
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Dispatcher, types
import sqlite3

class FSMOrder(StatesGroup):
    number = State()
    address = State()
    name = State()
    phone = State()
    
class FSMreview(StatesGroup):
    review = State()
    
async def start(message: types.Message):
    await message.answer('Здрасте.', reply_markup=kb_main)
    
async def cancel2(message: types.Message):
    await message.answer("Ок", reply_markup=kb_main)
async def cancel(message:types.Message, state: FSMContext):
    
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)
    
async def menu(message:types.Message):
    await message.reply("Выберете категорию", reply_markup=kb_menu)

async def hot(message:types.Message):
    await message.answer('''Название: Куриная грудка
Состав: Курица
Номер: №1''')
    await message.answer('''Название: Спагети
Состав: Мука
Номер:№2''')
    await message.answer('''Название: Судак
Состав: Мудак
Номер:№3''')
    await message.answer('''Название: Тудак
Состав: Судак
Номер:№4''')
    await message.answer('''Название: Утка Конфи
Состав: Утка
Номер:№5''')
    await message.answer('''Название: Пельмени
Состав: Мука, мясо, специи, бог
Номер:№6''',reply_markup= kb_menu)
async def snaks(message:types.Message):
    await message.answer('''Название: Куриные крылышки
Состав: Курица
Номер: №7''')
    await message.answer('''Название: Начос
Состав: Муки,Боль
Номер: №8''')
    await message.answer('''Название: Тосты
Состав: Мука, мясо, сыр
Номер: №9''')
    await message.answer('''Название: Фоккачо
Состав: Че?
Номер: №10''')
    await message.answer('''Название: Чесночные гренки
Состав: Хлеб, чеснок, специи
Номер: №11''',reply_markup=kb_menu)
    
async def deserts(message:types.Message):
    await message.answer('''Название: Фруктовое ассорти
Состав: Фрукты
Номер: №12''')
    await message.answer('''Название: Мороженое
Состав: Холод
Номер: №13''')
    await message.answer('''Название: Йогурт
Состав: Точно не соль
Номер: №14''')
    await message.answer('''Название: Виноград
Состав: азотистые вещества: белки, пептиды,
аминокислоты, амиды, органические основания,
аммонийные соли, нитраты; ферменты;
витамины и биокатализаторы; радиоактивные вещества
Номер: №15''', reply_markup=kb_menu)
    
async def drinks(message:types.Message):
    await message.answer('''Название: Сок
Состав: Фрукты
Номер: №16''')
    await message.answer('''Название: Кола
Состав: Кислота
Номер: №17''')
    await message.answer('''Название: Молоко
Состав: Лактоза
Номер: №18''')
    await message.answer('''Название: Коктейль
Состав: Icecream
Номер: №19''',reply_markup=kb_menu)

async def phones(message:types.Message):
    await message.answer('''Администратор: +375333546522
Тех.Поддержка: +375292352412''')
    
async def order(message:types.Message, state: FSMContext):
    await FSMOrder.number.set()
    await message.answer('Введите номер:', reply_markup= kb_cancel)

async def number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await FSMOrder.address.set()
    await message.answer('Введите адрес:')
    
async def address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
        await FSMOrder.name.set()
    await message.answer('Введите имя:')
     
async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMOrder.phone.set()
    await message.answer('Введите номер телефона: ')

async def phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        await message.answer("Сделано", reply_markup=kb_main)
    await state.finish()
    
async def review(message: types.Message, state: FSMContext):
    await FSMreview.review.set()
    await message.answer('Введите отзыв:', reply_markup = kb_cancel)

async def review2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['review'] = message.text
        rev = message.text
        re.addreview(rev)
        await message.answer('Спасибо за ваш отзыв!', reply_markup = kb_main)
    await state.finish()
    
async def showreview(message: types.Message):
    revi = re.GetTable()
    answer = ''
    for rev in revi:        
        answer = answer + 'Отзыв номер: №' + str(rev[0]) + '\n' +'Текст отзыва:' + str(rev[1]) + '\n'
    await message.answer(answer)
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(menu,Text(equals = 'Меню'))
    dp.register_message_handler(hot, Text(equals = 'Горячие блюда'))
    dp.register_message_handler(snaks, Text(equals = 'Закуски'))
    dp.register_message_handler(deserts, Text(equals = 'Десерты'))
    dp.register_message_handler(drinks, Text(equals = 'Напитки'))
    dp.callback_query_handler(cancel, commands = ['cancel'])
    dp.callback_query_handler(cancel, Text(equals='Отмена'), state = '*')
    dp.register_message_handler(order, Text(equals = 'Сделать заказ'), state = None)
    dp.register_message_handler(cancel2,Text(equals = 'Отмена'), state = None)
    dp.register_message_handler(phones, Text(equals='Телефоны для справки'), state = None)
    dp.register_message_handler(number, state = FSMOrder.number)
    dp.register_message_handler(address, state = FSMOrder.address)
    dp.register_message_handler(name, state = FSMOrder.name)
    dp.register_message_handler(phone, state = FSMOrder.phone)
    dp.register_message_handler(review, Text(equals = 'Оставить отзыв'), state=None)
    dp.register_message_handler(review2, Text, state = FSMreview)
    dp.register_message_handler(showreview, Text(equals= 'Посмотреть отзывы'), state = None)
    
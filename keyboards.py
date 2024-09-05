from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts import *

start_kb = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Расчет')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)


keyboard = [
    [
        InlineKeyboardButton(text=product1.name, callback_data='product_buying'),
        InlineKeyboardButton(text=product2.name, callback_data='product_buying'),
        InlineKeyboardButton(text=product3.name, callback_data='product_buying'),
        InlineKeyboardButton(text=product4.name, callback_data='product_buying'),
        InlineKeyboardButton(text=others, callback_data='other')
    ]
]
kb_catalog = InlineKeyboardMarkup(inline_keyboard=keyboard)


kb2 = InlineKeyboardMarkup()
button2 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button3 = InlineKeyboardButton(text='Формула расчета', callback_data='formulas')
kb2.add(button2)
kb2.add(button3)
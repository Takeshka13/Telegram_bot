from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

btn1 = KeyboardButton(text=LEXICON_RU['meow'])
btn2 = KeyboardButton(text=LEXICON_RU['best'])
btn3 = KeyboardButton(text=LEXICON_RU['cat'])
btn4 = KeyboardButton(text=LEXICON_RU['fox'])
btn5 = KeyboardButton(text=LEXICON_RU['game'])
btn6 = KeyboardButton(text=LEXICON_RU['anime'])

menu_kb_builder = ReplyKeyboardBuilder()

menu_kb_builder.row(btn1, btn2, btn3, btn4,  width=2)
menu_kb_builder.add(btn5)
menu_kb_builder.add(btn6)

menu_kb: ReplyKeyboardMarkup = menu_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)

r1 = KeyboardButton(text=LEXICON_RU['Yes'])
r2 = KeyboardButton(text=LEXICON_RU['No'])
r3 = KeyboardButton(text=LEXICON_RU['Love'])
r4 = KeyboardButton(text=LEXICON_RU['Airkiss'])
r5 = KeyboardButton(text=LEXICON_RU['Laugh'])
r6 = KeyboardButton(text=LEXICON_RU['Evillaugh'])
r7 = KeyboardButton(text=LEXICON_RU['Sorry'])
r8 = KeyboardButton(text=LEXICON_RU['Sleep'])
r9 = KeyboardButton(text=LEXICON_RU['Cry'])
r10 = KeyboardButton(text=LEXICON_RU['Happy'])

filter_kb_builder = ReplyKeyboardBuilder()

filter_kb_builder.row(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, width=2)

filter_kb: ReplyKeyboardMarkup = filter_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)


button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True)

button_r = KeyboardButton(text=LEXICON_RU['rock'])
button_s = KeyboardButton(text=LEXICON_RU['scissors'])
button_p = KeyboardButton(text=LEXICON_RU['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_r],
              [button_s],
              [button_p]],
    resize_keyboard=True)
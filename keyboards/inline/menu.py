from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌫 Биз ҳақимизда', callback_data='about'),
            InlineKeyboardButton(text='✍ ️Aриза қолдириш', callback_data='send'),
        ]
    ]
)

menu_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✍ ️Aриза қолдириш', callback_data='send'),
        ]
    ]
)

about_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Олий талим', callback_data='oliy'),
            InlineKeyboardButton(text='Ўрта талим', callback_data='orta'),
        ]
    ]
)

about_bridge = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Турмуш қурган', callback_data='uylangan'),
            InlineKeyboardButton(text='Турмуш қурмаган', callback_data='uylanmagan'),
        ]
    ]
)

play = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Аризангизни Тасдиқланг', callback_data='tastiqlash'),

        ]
    ]
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Location', request_location=True)
        ],
    ], resize_keyboard=True
)

accept = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рухсат бериш')
        ],
    ], resize_keyboard=True
)

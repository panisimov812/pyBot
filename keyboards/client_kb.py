from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

btn_open_hours = KeyboardButton('/Режим_работы')
btn_location = KeyboardButton('/Расположение')
btn_menu = KeyboardButton('/Меню')
# btn_contact = KeyboardButton('/Контакты', request_contact=True)
# btn_myLocation = KeyboardButton('/Поделиться где я',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(btn_open_hours).add(btn_location).insert(btn_menu)  # .row(btn_contact,btn_myLocation)
# kb_client.add(btn_open_hours).add(btn_location).add(btn_menu)  #расположение друг под другом
# kb_client.row(btn_menu,btn_location,btn_open_hours)            #расположение в строку

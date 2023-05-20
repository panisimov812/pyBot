from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

btnOpenHours = KeyboardButton('/Режим_работы')
btnLocation = KeyboardButton('/Расположение')
btnMenu = KeyboardButton('/Меню')
#btnContact = KeyboardButton('/Контакты', request_contact=True)
#btnMyLocation = KeyboardButton('/Поделиться где я',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(btnOpenHours).add(btnLocation).insert(btnMenu)#.row(btnContact,btnMyLocation)
#kb_client.add(btnOpenHours).add(btnLocation).add(btnMenu)  #расположение друг под другом
#kb_client.row(btnMenu,btnLocation,btnOpenHours)            #расположение в строку


#Программа для сборки пекеджей баз валют
def print_num():
    print('12')
from builder_modules import *
from tkinter import *
#Создаем приложение
tk = Tk()
tk.title("Currency package builder")
tk.resizable(0, 0)
tk.iconbitmap("title_image.ico")
canvas = Canvas(tk, width=600, height=600,  highlightthickness=0)
canvas.pack()

#Весь функционал кнопки сборки
#Указываем путь к файлам сборки необходимого устройства
path = r'C:\SVN_Projects\NOTEBASE\D820\VARIANT'

#Необходимое расширение
extension = '.lua'

#Находим файлы с расширением .lua
#list_of_lua_files = list_of_fils(path, extension)

#Вибираем валюту с измененной базой
#*************************
currency = '{ \"UZS\"'
#*************************

#Находим список скриптов для запуска
#scripts_for_launching = files_for_start(list_of_lua_files, currency)

#Добавляем кнопку для сборки пекеджей
builder_button = Button(tk, text='build', command=print_num)
builder_button.pack()

tk.mainloop()
#Указываем путь к файлам сборки необходимого устройства
#path = r'C:\SVN_Projects\NOTEBASE\D820\VARIANT'
#Необходимое расширение
#extension = '.lua'
#Находим файлы с расширением .lua
#list_of_lua_files = builder_modules.list_of_fils(path, extension)
#Вибираем валюту с измененной базой
#*************************
#currency = '{ \"UZS\"'
#*************************
#Находим список скриптов для запуска
#scripts_for_launching = builder_modules.files_for_start(list_of_lua_files, currency)
#Пересобираем выбранные скрипты
#building = builder_modules.scripts_running(scripts_for_launching)

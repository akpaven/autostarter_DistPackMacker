#Программа для сборки пекеджей баз валют
from builder_modules import *
from tkinter import *

#Создаем приложение
tk = Tk()
tk.title("Currency package builder")
tk.resizable(0, 0)
tk.iconbitmap("title_image.ico")
canvas = Canvas(tk, width=300, height=50,  highlightthickness=0)
canvas.pack()

#Создаем поле ввода пути к папкам скриптов для выбранного устройства путем введения его названия
path_title = Label(tk, text='Device model:', fg='green', font=('Verdana', 10)).pack()
path_entry = Entry(tk, width=10, fg='blue', font=('Verdana', 10)).pack()

#Указываем путь к файлам сборки необходимого устройства
path = r'C:\SVN_Projects\NOTEBASE\D820\VARIANT'

#Необходимое расширение
extension = '.lua'

#Создаем поле ввода валюты
currency_title = Label(tk, text='Currency name:', fg='green', font=('Verdana', 10)).pack()
currency_entry = Entry(tk, width=5, fg='blue', font=('Verdana', 10)).pack()

#Вибираем валюту с измененной базой
#*************************
currency = '{ \"UZS\"'
#*************************

#Находим файлы с расширением .lua
list_of_lua_files = list_of_fils(path, extension)

#Находим список скриптов для запуска
scripts_for_launching = files_for_start(list_of_lua_files, currency)

#Добавляем кнопку для сборки пекеджей
builder_button = Button(tk, text='build', command=lambda scrip=scripts_for_launching: scripts_running(scrip))
builder_button.pack()

tk.mainloop()


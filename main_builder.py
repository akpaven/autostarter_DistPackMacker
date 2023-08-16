import builder_modules

#Указываем путь к файлам сборки необходимого устройства
path = r'C:\SVN_Projects\NOTEBASE\D820M1\VARIANT'
#Необходимое расширение
extension = '.lua'
#Находим файлы с расширением .lua
list_of_lua_files = builder_modules.list_of_fils(path, extension)
#Вибираем валюту с измененной базой
#*************************
currency = '{ \"RUB\"'
#*************************
#Находим список скриптов для запуска
scripts_for_launching = builder_modules.files_for_start(list_of_lua_files, currency)
#Пересобираем выбранные скрипты
building = builder_modules.scripts_running(scripts_for_launching)

import os
import subprocess

#Функция поиска файлов по определенному пути с выбранным расширением
def list_of_fils(abs_dir, extension):
    filelist = []
    #scandir работает в 10 раз быстрее
    for subdir, dirs, files in os.walk(abs_dir):
            for file in files:
                #print os.path.join(subdir, file)
                filepath = subdir + os.sep + file
                if filepath.endswith(extension):
                    filelist.append(filepath)
    return filelist



#Функция проверяет нахождение необходимой строки в файлах и возврощает
# список таких файлов

def files_for_start(list, currency):
    files_for_launching = []
    for path in list:
        opened_file = open(path, errors='ignore')
        readed_file = opened_file.read()
        if currency in readed_file:
            files_for_launching.append(path)
        else:
            continue
    return files_for_launching


#Функция запуска скриптов программой DistrPkg Maker
def scripts_running(list):
    program = "C:\SVN_Projects\BVS\Software\DistrPkg Maker\DistrPkgMaker.exe"
    for string in list:
        process = subprocess.Popen([program, string])
        code = process.poll()














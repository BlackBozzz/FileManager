import os
import shutil

global HomePath

def Help():
    return ("""
    CreateNewFolder - создать пустой каталог (папку)
    DeleteFolder - удалить папку
    FolderLevelUp - вернуться в предыдущую директорию
    MoveToFolder - перейти в другой каталог
    CreateNewFile - создать новый текстовый файл
    WriteInFile - записать текст в файл
    ShowFile - вывести содержимое файла
    DeleteFile - удалить  файл
    CopyFile - копировать файл
    MoveFile - заменить (переместить) этот файл в другой каталог
    RenameFile - переименовать файл или каталог
    """)


def WorkPath(user_name):
    global HomePath
    HomePath = f"{HomePath}/{user_name}"
    try:
        os.chdir(HomePath)
    except FileNotFoundError:
        os.mkdir(HomePath)
        os.chdir(HomePath)


def CheckPath(path):
    global HomePath
    if len(path.split("/")) == 1:
        if HomePath in os.getcwd():
            return True
    else:
        if HomePath in path[:len(HomePath)]:
            return True
    return False


# создать пустой каталог (папку)
def CreateNewFolder(folder):
    try:
        if not os.path.isdir(str(folder)) and CheckPath(folder):
            os.mkdir(str(folder))
        else:
            print("Нет разрешения")
    except FileExistsError:
        print("Файл с таким именем уже существует")


# удалить папку
def DeleteFolder(folder):
    if CheckPath(folder):
        os.rmdir(str(folder))
    else:
        print("Нет разрешения")


# вернуться в предыдущую директорию
def FolderLevelUp():
    if os.getcwd() != HomePath:
        os.chdir("..")
    else:
        print("Нет разрешения")


# перейти в другой каталог
def MoveToFolder(path):
    if CheckPath(path):
        os.chdir(path)
        print(os.getcwd())
    else:
        print(os.getcwd())
        print("Нет разрешения")


# создать новый текстовый файл
def CreateNewFile(file):
    try:
        if CheckPath(file):
            text_file = open(f"{file}", "w")
            text_file.close()
        else:
            print("Нет разрешения")
    except FileExistsError:
        print("Файл с таким именем уже существует")


# записать текст в этот файл
def WriteInFile(file):
    if CheckPath(file):
        with open(f"{file}", "a") as file:
            file.write(input("Введите текст для записи в файл\n"))
    else:
        print("Нет разрешения")


# вывести содержимое файла
def ShowFile(file):
    if CheckPath(file):
        with open(f"{file}", "r") as file:
            for line in file:
                print(line)
    else:
        print("Нет разрешения")


# удалить этот файл
def DeleteFile(file):
    if CheckPath(file):
        os.remove(f"{file}")
    else:
        print("Нет разрешения")


# копировать файл
def CopyFile(file, path):
    if CheckPath(file) and CheckPath(path):
        shutil.copy(fr"{file}", f"{path}")
    else:
        print("Нет разрешения")


# заменить (переместить) этот файл в другой каталог
def MoveFile(file, path):
    if CheckPath(file) and CheckPath(path):
        os.replace(fr"{file}", f"{path}/{file.split('/')[-1]}")
    else:
        print("Нет разрешения")


# переименовать
def RenameFile(file, new_file):
    if CheckPath(file):
        if len(file.split("/")) == 1:
            if len(new_file.split("/")) == 1:
                os.rename(f"{file}", f"{new_file}")
        else:
            if len(new_file.split("/")) == 1:
                os.rename(f"{file}", f"{file[:-len(file.split('/')[-1])]}/{new_file}")
    else:
        print("Нет разрешения")

def Registration():
    global HomePath
    FilesPath = os.getcwd()
    with open(f"{FilesPath}/Settings", "r") as file:
        HomePath = file.read()
    os.chdir(HomePath)

    # Получение списка зарегистрированных пользователей
    with open(f"{FilesPath}/users", "r") as file:
        users = [name.split() for name in file.readlines()]

    user_name = input("Введите имя: ")

    Reg = False

    for user in users:
        if user_name == user[0]:
            password = input("Введите пароль: ")
            while password != user[1]:
                print("Неверный пароль")
                password = input("Введите пароль: ")
            Reg = True
            break

    if not Reg:
        password = input("Придумайте пароль: ")
        users.append([user_name, password])
        with open(f"{FilesPath}/users", "w") as file:
            for user in users:
                file.write(" ".join(user) + "\n")

    WorkPath(user_name)

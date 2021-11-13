from Functions import *

if __name__ == "__main__":
    Registration()
    while True:
        choose = input("Введите команду с аргументами через пробел: ")
        Command = choose.split()
        print(Command)
        try:
            if Command[0] == "help":
                print(Help())

            elif Command[0] == "CreateNewFolder":
                CreateNewFolder(Command[1])

            elif Command[0] == "DeleteFolder":
                DeleteFolder(Command[1])

            elif Command[0] == "FolderLevelUp":
                FolderLevelUp()

            elif Command[0] == "MoveToFolder":
                MoveToFolder(Command[1])

            elif Command[0] == "CreateNewFile":
                CreateNewFile(Command[1])

            elif Command[0] == "WriteInFile":
                WriteInFile(Command[1])

            elif Command[0] == "ShowFile":
                ShowFile(Command[1])

            elif Command[0] == "DeleteFile":
                DeleteFile(Command[1])

            elif Command[0] == "CopyFile":
                CopyFile(Command[1], Command[2])

            elif Command[0] == "MoveFile":
                MoveFile(Command[1], Command[2])

            elif Command[0] == "RenameFile":
                RenameFile(Command[1], Command[2])

            else:
                print("Неизвестная команда\nВведите: help, для просмотра команд")


        except IndexError:
            print("Неизвестная команда\nВведите: help, для просмотра команд")


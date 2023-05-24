def read_file():
    with open('base.txt', 'r+', encoding="utf-8") as file:
        return file.read()

def write_file(string):
    with open('base.txt', 'a', encoding="utf-8") as file:
        file.write(string + "\n")

def ShowBase():
    print("_________________________________________________")
    for user in read_file().split('\n'):
        print(user)
    print("_________________________________________________")

def GetUser():
    sname = input("Введите Фамилию: " + "\n") + " "
    name = input("Введите Имя: " + "\n") + " "
    fname = input("Введите Отчество: " + "\n") + " "
    number = input("Введите номер: " + "\n") + " "
    return (sname + name + fname + number)

def EditBase():
    print("_________________________________________________")
    write_file(GetUser())
    print("_________________________________________________")

def FindInBase():
    print("_________________________________________________")
    element = input("Введите одну из характеристик записи для поиска: " + "\n")
    for user in read_file().split("\n"):
        for userDetail in user.split():
            if userDetail.lower() == element.lower():
                    print("Нашел: " +  user)
    print("_________________________________________________")
def Main():
    ShowBase()
    print("Если хотите добавлять данные, напишите 'add' или 'добавить'")
    print("Если хотите найти какую то запись, напишите 'search' или 'найти'")
    print("Если хотите выйти из программы, напишите 'end' или 'закончить'")
    string = input()
    if string == 'add' or string == 'добавить':
        EditBase()
    if string == 'search' or string == 'найти':
        FindInBase()
    if string == 'end' or string == 'закончить':
        return 'end'

while True:
    if Main() == 'end':
        break
    else:
        Main()
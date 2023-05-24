def ShowBase():
    with open('base.txt', 'r', encoding="utf-8") as file:
        print("_________________________________________________")
        while True:
            user = file.readline()
            if not user:
                break
            else:
                print(user)
        print("_________________________________________________")

def EditBase():
    with open('base.txt', 'a', encoding="utf-8") as file:
        print("_________________________________________________")
        string = input("Введите данные в формате 'Фамилия Имя Отчество номер телефона': " + "\n")
        if not string:
            ShowBase()
        else:
            file.write("\n" + string)
        print("_________________________________________________")
    ShowBase()

def FindInBase():
    with open('base.txt', 'r', encoding="utf-8") as file:
        print("_________________________________________________")
        element = input("Введите одну из характеристик записи для поиска: " + "\n")
        while True:
            el = file.readline().split()
            for i in el:
                if i.lower() == element.lower():
                    print("Нашел:" + str.join(" ", el))
            if not el:
                break
        print("_________________________________________________")
def Main():
    ShowBase()
    print("Если хотите добавлять данные, напишите 'add' или 'добавить'")
    print("Если хотите найти какую то запись, напишите 'search' или 'найти'")
    string = input()
    if string == 'add' or string == 'добавить':
        EditBase()
    if string == 'search' or string == 'найти':
        FindInBase()

while True:
    Main()
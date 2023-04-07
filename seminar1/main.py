def Task1():
    n1 = int(input('Input first  num'))
    n2 = int(input('Input second  num'))
    n3 = int(input('Input third  num'))
    print(f'Summ of nums: {n1 + n2 + n3}')


def Task2():
    n1 = int(input('First side'))
    n2 = int(input('Second side'))
    print(f'P:{n1 * n2}')


def Task3():
    n1 = int(input('First num'))
    n2 = int(input('Second num'))
    if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
        print(True)
    else:
        print(False)


def Task4():
    n1 = int(input('Input first  num'))
    n2 = int(input('Input second  num'))
    n3 = int(input('Input third  num'))
    if n1 > 0 or n2 > 0 or n3 > 0:
        print(True)
    else:
        print(False)


def Task5():
    n1 = int(input('First num'))
    n2 = int(input('Second num'))
    if n1 > n2:
        print(n2)
    elif n1 == n2:
        print('n1 = n2')
    else:
        print(n1)


def Task6():
    n = input('Input num')
    if len(n) == 4:
        print('Yes')
    else:
        print('No')

def STask1():
    n = int(input('Input km/day'))
    m = int(input('Input way km'))
    S = -m // n * -1
    print(S)

def STask3():
    class1 = int(input('Students in first class'))
    class2 = int(input('Students in second class'))
    class3 = int(input('Students in third class'))
    students = class1 + class2 + class3
    desks = students // 2 + students % 2
    print(desks)

def STask5():
    i = int(input('Vitya Vagon num'))
    j = int(input('Vagon num'))
    if i == j:
        print('Need More Information')
    else:
        print(i + j - 1)

def STask7():
    year = int(input('Input year'))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Yes')
    else:
        print('No')

def STask2():
    num = input('Input num')
    s = 0
    for i in num:
        s += int(i)
    print(s)

def STask4():
    S = int(input('Input nums of birds'))
    if S % 6 == 0:
        print(f'Petya and Sergey make { S // 6 } birds each one, Katya make {S // 6 * 4} birds')
    else:
        print('They cant do thoose nums of birds')

def STask6():
    ticket = input('Input num of ticket')
    t1 = 0
    t2 = 0
    i = 0
    if len(ticket) != 6:
        print('This is not ticket num')
    else:
        while i < len(ticket):
            if i < len(ticket) / 2:
                t1 += int(ticket[i])
            else:
                t2 += int(ticket[i])
            i = i + 1
        if t1 == t2:
            print('This ticket is lucky')
        else:
            print('This ticket is unlucky')

def STask8():
    n = int(input('Input second side of chokolade'))
    m = int(input('Input first side of chokolade'))
    k = int(input('Input count of part of chokolade'))
    if k % m == 0 or k % n == 0:
        print('Yes')
    else:
        print('No')

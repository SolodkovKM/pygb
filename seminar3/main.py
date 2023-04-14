import random


def STask17():
    listn = list()
    count = 0
    while True:
        n = int(input("Input num: "))
        listn.append(n)
        if listn.count(n) == 1:
            count += 1
        print(count)
        print(listn)


def STask19():
    listn = list()
    for i in range(0, 10):
        listn.append(random.randint(0, 10))
    k = int(input("Input K: "))
    print(listn)
    listn = listn[k:] + listn[:k]
    print(listn)

dict = {'V' : '124', 'VI' : '124', 'VII' : '643', 'VIII' : '613', 'IX' : '37458', 'X' : '513'}
def Stask21(dict):
    a = set()
    for i in dict.values():
        a.add(i)
    print(a)

def STask23():
    listn = list()
    for i in range(0, 10):
        listn.append(random.randint(-10, 10))
    print(listn)
    listt = list()
    count = 0
    for i in range(len(listn)-1):
        if listn[i] < listn[i + 1]:
            count += 1
            listt.append(f'{listn[i]} < {listn[i + 1]}')
    print(f'{count} {tuple(listt)}')


def ST1():
    listn = list()
    for i in range(0, 10):
        listn.append(random.randint(-10, 10))
    print(listn)
    for i in range(len(listn)-2, 0, -1):
        if listn[i - 1] < listn[i] > listn[i + 1]:
            print(i, listn[i])
            break


def HTask16():
    N = int(input("Input N: "))
    listn = list()
    for i in range(0, N):
        listn.append(int(input(f'Input num {i+1}: ')))
    X = int(input("Input X: "))
    print(listn.count(X))
    print(listn)

def HTask18():
    N = int(input("Input N: "))
    listn = list()
    for i in range(0, N):
        listn.append(int(input(f'Input num {i+1}: ')))
    X = int(input("Input X: "))
    listn.sort()
    minnum = listn[0]
    maxnum = listn[len(listn)-1]
    for i in listn:
        if minnum < i < X:
            minnum = i
        if maxnum > i > X:
            maxnum = i
    if X - minnum > maxnum - X:
        print(maxnum)
    else:
        print(minnum)

def HTask20():
    dict = {'A': 1, 'B': 3, 'C': 3,
            'D': 2, 'E': 1, 'F': 4,
            'G': 2, 'H': 4, 'J': 8,
            'K': 5, 'L': 1, 'M': 3,
            'N': 1, 'O': 1, 'P': 3,
            'Q': 10, 'R': 1, 'S': 1,
            'T': 1, 'U': 1, 'V': 4,
            'W': 4, 'X': 8, 'Y': 4,
            'Z': 10, 'А': 1, 'Б': 3,
            'В': 1, 'Г': 3, 'Д': 2,
            'Е': 1, 'Ё': 3, 'Ж': 5,
            'З': 5, 'И': 1, 'Й': 4,
            'К': 2, 'Л': 2, 'М': 2,
            'Н': 1, 'О': 1, 'П': 2,
            'Р': 1, 'С': 1, 'Т': 1,
            'У': 2, 'Ф': 10, 'Х': 5,
            'Ц': 5, 'Ч': 5, 'Ш': 8,
            'Щ': 10, 'Ъ': 10, 'Ы': 4,
            'Ь': 3, 'Э': 8, 'Ю': 8, 'Я':3}
    word = input("Input word: ")
    sum = 0
    for i in word:
        sum += dict.get(i.upper())
    print(sum)


import random


def Task9():
    n = int(input("Input n: "))
    fact = 1
    while n >= 0:
        fact *= n
        n -= 1
        if n == 0:
            print(fact)
            break
    else:
         print(1)

def Task11():
    a = int(input("Input A: "))
    fib = [0, 1]
    while fib[len(fib) - 1] < a:
        fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
    if a != fib[len(fib)-1]:
        print(-1)
    else:
        print(len(fib))


def Task11_2():
    a = int(input("Input A: "))
    fiba = 0
    fibb = 1
    count = 2
    while fibb < a:
        fibc = fiba + fibb
        fiba = fibb
        fibb = fibc
        count += 1
    if a != fibb:
        print(-1)
    else:
        print(count)

def Task13():
    len = int(input("Input count of days: "))
    temper = list()
    for _ in range(0, len):
        temper.append(int(input()))
    print(temper, end=' ')
    temper.append(-5)
    count = 0
    max = 0
    for i in temper:
        if i > 0:
            count += 1
        else:
            if max <= count:
                max = count
            count = 0
    print(max)


def Task15():
    len = int(input("Input count of arbuzes: "))
    arbuzes = list()
    for _ in range(0, len):
        arbuzes.append(random.randint(1, 10))
    print(arbuzes)
    min = arbuzes[0]
    max = min
    for el in arbuzes:
        if el < min:
            min = el
        if el > max:
            max = el
    print(min , max)

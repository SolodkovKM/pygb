import time


def STask25():
    start = time.perf_counter()

    count = 0
    lens = len(string)
    while lens > 0:
        for i in range(0, lens):
            if string[0] == string[i]:
                count += 1
        lens -= count
        print(f'{string[0]} -> {count}')
        string = string.replace(string[0], '')
        count = 0
    end = time.perf_counter()
    duration = end - start

def STask252():
    start = time.perf_counter()
    for i in set(string):
        print(string.count(i))
    end = time.perf_counter()
    duration = end - start
def TASK():
    text = input(':')
    count = 0
    sw = False
    for i in range(0, len(text)):
        if text[i] != ' ' or text[i] != '\n':
            sw = True
            print(sw, text[i])
            while text[i] == ' ' or text[i] == '\n':
                sw = False
                print(sw, text[i])
                count += 1
                break
    print(count)

TASK()

string = input(": ")
start = time.perf_counter()
count = 0
lens = len(string)
while lens > 0:
    for i in range(0, lens):
        if string[0] == string[i]:
            count += 1
    lens -= count
    print(f'{string[0]} -> {count}')
    string = string.replace(string[0], '')
    count = 0
end = time.perf_counter()
duration = end - start

start2 = time.perf_counter()
for i in set(string):
    print(string.count(i))
end2 = time.perf_counter()
duration2 = end2 - start2

print(duration/duration2)
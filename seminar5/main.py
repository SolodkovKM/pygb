def PowN(a, b):
    if b > 1:
        a = a * PowN(a, b - 1)
    return a
a = 2
b = 6
#print(f'A: {a}; B: {b} -> {PowN(a, b)}')

def Task6(string):
    if not string.isupper():
        print("Not valid string")
    else:
        slen = len(string)
        result = string[0]
        letter = string[0]
        count = 1
        for i in range(0, slen):
            if string[i] != letter:
                letter = string[i]
                if count == 1:
                    result += letter
                else:
                    result += str(count) + letter
                count = 1
            else:
                count += 1
        if count != 1:
            result += str(count)
        print(result)
Task6("AAABBBAABBAFFFDD")
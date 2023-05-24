def FindAnton():
    #n = int(input("Input: "))
    strings = list()
    result = set()
    word = 'anton'
    #for i in range(0, n):
        #strings.append(input("Input string:"))
    strings.append("asfasfasfasnfasfasftfadsafsadofsadfsadfnasdf")
    strings.append("anton")
    strings.append("asdgasdgasdkgasdg")
    strings.append("asfgdfgsdgdgdsgjdsg")
    strings.append("asadasdnasfaasfasftasfasfogsdgdn")
    for i in range(0, len(strings)):
        halfres = ''
        for j in word:
            if j in strings[i]:
                halfres += j
        if halfres == word:
            result.add(i)
    print(result)

def Task30():
    
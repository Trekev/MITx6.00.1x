#Problem 2

def findbob(s):
    s = s + "000"
    s=list(s)

    count = 0
    for i in range(len(s)):
        if s[i] == 'b' and s[i+1]=='o' and s[i+2]=='b':
            count += 1
    print('Number of times bob occurs is: '+ str(count))


def longestalpha(s):
    s = s + 'z'
    s = list(s)
    alphalist = []
    for i in range(len(s)): s[i] = (ord(s[i]) - 96)

    for i in range(len(s)):
        try:
            if s[i] <= s[i+1]:
                alphalist.append(s[i])
        except:
            continue
    for i in range(len(alphalist)): alphalist[i] = chr(alphalist[i]+96)
    print(alphalist)
    print(s)


longestalpha('abc')
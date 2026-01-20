eng = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
ENG = eng.upper()


def english_word(m):
    st = 0
    for i in m:
        if i.isalnum():
            st += 1
    li = []
    for i in range(len(m)):
        if m[i].isalpha():
            if m[i] in eng:
                a = eng.find(m[i])
                li.append(eng[a + st])
            elif m[i] in ENG:
                a = ENG.find(m[i])
                li.append(ENG[a + st])
        else:
            li.append(m[i])
    return "".join(li)


mess = input("Введите предложение на англйиском \n").split()
for i in range(len(mess)):
    mess[i] = english_word(mess[i])

print(*mess)

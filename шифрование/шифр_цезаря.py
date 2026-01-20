"""шифрует или расшифровывает английское или русское сообщение с помощью шифра Цезаря"""

eng = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
ENG = eng.upper()
ru = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
RU = ru.upper()
dir = input("Укажите направление: ")
lan = input("Укажите язык: ")


mess = input()


def english(m, dir, st):
    st = int(st)
    st = st % 26
    li = []
    if "де" in dir.lower():
        for i in range(len(m)):
            if m[i].isalpha():
                if m[i] in eng:
                    a = eng.rfind(m[i])
                    li.append(eng[a-st])
                elif m[i] in ENG:
                    a = ENG.rfind(m[i])
                    li.append(ENG[a-st])
            else:
                li.append(m[i])
    else:
        for i in range(len(m)):
            if m[i].isalpha():
                if m[i] in eng:
                    a = eng.find(m[i])
                    li.append(eng[a+st])
                elif m[i] in ENG:
                    a = ENG.find(m[i])
                    li.append(ENG[a+st])
            else:
                li.append(m[i])
    return "".join(li)

def russian(m, dir, st):
    li=[]
    st=int(st)
    st = st % 32
    if "де" in dir.lower():
        for i in range(len(m)):
            if m[i].isalpha():
                if m[i] in ru:
                    a = ru.rfind(m[i])
                    li.append(ru[a-st])
                elif m[i] in RU:
                    a = RU.rfind(m[i])
                    li.append(RU[a-st])

            else:
                li.append(m[i])
    else:
        for i in range(len(m)):
            if m[i].isalpha():
                if m[i] in ru:
                    a = ru.find(m[i])
                    li.append(ru[a+st])
                elif m[i] in RU:
                    a = RU.find(m[i])
                    li.append(RU[a+st])
            else:
                li.append(m[i])
    return "".join(li)

if "р" in lan:
    for step in range(1,26):
        print(russian(mess, dir, step))
else:
    for step in range(1,26):
        print(english(mess, dir, step))


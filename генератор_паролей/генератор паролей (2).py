import random as r
import string as s


def generate_password(length):
    nec = set(s.ascii_letters + s.digits) - set("01oOlI")
    while True:
        a = r.sample(list(nec), length)
        e = "".join(a)
        if e.upper() == e or e.lower() == e or e.lower() == e.upper():
            continue
        else:
            return e


def generate_passwords(count, length):
    li = [generate_password(length) for _ in range(count)]
    return li


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep="\n")

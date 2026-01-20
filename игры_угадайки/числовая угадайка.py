print("Добро пожаловать в числовую угадайку")


def is_valid(q, n):
    if int(q) in range(1, n + 1):
        return True
    else:
        return False


def guess_number():
    import random

    print("Введите верхнюю границу")
    n = int(input())
    num = random.randint(1, n)
    cnt = 0
    while True:
        print(f"Ведите число от 1 до {n}")
        a = input()
        cnt += 1
        if not is_valid(a, n):
            print(f"А может быть все-таки введем целое число от 1 до {n}?")
        else:
            a = int(a)
            if a < num:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif a > num:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!")
                break
    print("Количество попыток:", cnt)
    print("Будем играть еще раз?")
    if input().lower() == "да":
        guess_number()
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


guess_number()

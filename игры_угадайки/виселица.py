"""игра Виселица. Пользователь угадывает слово. Пользователь может назвать не ту букву не более 6 раз"""

import random

word_list = ["корова", "собака", "лисица","медведь","кролик", "шиншилла"]


def get_word(q):
    word = random.choice(q)
    return word 

def zashita_ot_duraka(w):
    while not w.isalpha():
        print("Ты че дурак? введи букву или слово!")
        w=input()
    return w
    
    


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play():
    
    word = get_word(word_list)
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print(word)
    while tries>0:
        print(display_hangman(tries))
        print(word_completion)
        lw = input("Введите букву или слово: ")
        lw = zashita_ot_duraka(lw)
        if len(lw) ==1:
            if lw in guessed_letters:
                continue
            if lw in word:
                li = list(word_completion)
                for i in range(len(word)):
                    if lw==word[i]:
                        li[i] = lw        
                word_completion = "".join(li)
                if word_completion==word:
                    print(word)
                    print("Поздравляем, вы угадали слово! Вы победили!")
                    guessed=True
                    break 
            else:
                tries-=1
            guessed_letters.append(lw)
        
        else:
            if lw==word:
                print("Поздравляем, вы угадали слово! Вы победили!")
                guessed=True
                break
            else:    
                if lw not in guessed_words:
                    tries -=1
                       
                else:
                    continue            
        
            guessed_words.append(lw)
    if guessed ==False:
        print(display_hangman(tries))
        print("Слово:", word)
        print("Вы проиграли!") 
    
play()

while True:
    print("Хотите сыграть еще раз?")
    a = input()
    if a== "yes" or a=="да":
        play()
    else:
        print("Спасибо за игру!")
        break

        





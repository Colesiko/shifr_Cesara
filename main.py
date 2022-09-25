print("Программа для зашифровки и расшифровки методом Цезаря на русском или английском языках")
alphabet1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphabet2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a = 123
while a != 0:
    print("Напишите 1 для зашифровки, напишите 2 для расшифровки, напишите 0 чтобы закончить: ")
    a = int(input())
    if a == 1:
        print("Введиде слово для зашифровки: ")
        word = input()
        word = word.lower()
        if word[0] in alphabet1:
            print("Введите шаг шифровки: ")
            step = int(input())
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alphabet1.find(i)
                newpos = pos + step
                newword += alphabet1[newpos]
            print("Ваше зашифрованное слово: " + newword)
        elif word[0] in alphabet2:
            print("Введите шаг шифровки: ")
            step = int(input())
            if step > 32:
                step %= 32
            newword = ""
            for i in word:
                pos = alphabet2.find(i)
                newpos = pos + step
                newword += alphabet2[newpos]
            print("Ваше зашифрованное слово: " + newword)
        else:
            print("Вы ввели не слово")
    elif a == 2:
        print("Введиде слово для расшифровки: ")
        word = input()
        word = word.lower()
        if word[0] in alphabet1:
            print("Введите шаг шифровки: ")
            step = int(input())
            if step > 25:
                step %= 25
            newword = ""
            for i in word:
                pos = alphabet1.find(i)
                newpos = pos - step
                newword += alphabet1[newpos]
            print("Ваше расшифрованное слово: " + newword)
        elif word[0] in alphabet2:
            print("Введите шаг шифровки: ")
            step = int(input())
            if step > 32:
                step %= 32
            newword = ""
            for i in word:
                pos = alphabet2.find(i)
                newpos = pos - step
                newword += alphabet2[newpos]
            print("Ваше расшифрованное слово: " + newword)
        else:
            print("Вы ввели не слово")
    if a == 0:
        break
print("Программа для зашифровки и расшифровки методом Цезаря на русском или английском языках")
alphavit1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphavit2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a = 123
while a != 0:
    print("Напишите 1 для зашифровки, напишите 2 для расшифровки, напишите 0 чтобы закончить: ")
    a = int(input())

    if a == 1:
        print("Введиде слово для зашифровки: ")
        slovo = input()
        slovo = slovo.lower()

        if slovo[0] in alphavit1:
            print("Введите шаг шифровки: ")
            shag = int(input())

            if shag > 25:
                shag %= 25
            newslovo = ""

            for i in slovo:
                pos = alphavit1.find(i)
                newpos = pos + shag
                newslovo += alphavit1[newpos]
            print("Ваше зашифрованное слово: " + newslovo)

        elif slovo[0] in alphavit2:
            print("Введите шаг шифровки: ")
            shag = int(input())

            if shag > 32:
                shag %= 32
            newslovo = ""

            for i in slovo:
                pos = alphavit2.find(i)
                newpos = pos + shag
                newslovo += alphavit2[newpos]
            print("Ваше зашифрованное слово: " + newslovo)

        else:
            print("Вы ввели не слово")

    elif a == 2:
        print("Введиде слово для расшифровки: ")
        slovo = input()
        slovo = slovo.lower()

        if slovo[0] in alphavit1:
            print("Введите шаг шифровки: ")
            shag = int(input())

            if shag > 25:
                shag %= 25
            newslovo = ""

            for i in slovo:
                pos = alphavit1.find(i)
                newpos = pos - shag
                newslovo += alphavit1[newpos]
            print("Ваше расшифрованное слово: " + newslovo)

        elif slovo[0] in alphavit2:
            print("Введите шаг шифровки: ")
            shag = int(input())

            if shag > 32:
                shag %= 32
            newslovo = ""

            for i in slovo:
                pos = alphavit2.find(i)
                newpos = pos - shag
                newslovo += alphavit2[newpos]
            print("Ваше расшифрованное слово: " + newslovo)

        else:
            print("Вы ввели не слово")

    if a == 0:
        break
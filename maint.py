alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
while True:
    f = ""
    b = input("Введите строку для шифрования/дешифрования: ")
    e = int(input("Введите число символов для сдвига: "))
    m = input("Введите + или - (сдвиг вправо или влево): ")
    if m == "+":
        if e > 33:
            l = int(e / 33)
            for i in b:
                if i == " ":
                    f += i
                else:
                    f += alp[alp.index(i) + (e - 33 * l)]
            print(f)
        else:
            for i in b:
                if i == " ":
                    f += i
                else:
                    f += alp[alp.index(i) + e]
            print(f)
    elif m == "-":
        if e > 33:
            l = int(e / 33)
            for i in b:
                if i == " ":
                    f += i
                else:
                    f += alp[alp.index(i) + (33 * (l + 1) - e)]
            print(f)
        else:
            for i in b:
                if i == " ":
                    f += i
                else:
                    f += alp[alp.index(i) + (33 - e)]
            print(f)
    else:
        print("Неправильный ввод. Попробуйте ещё раз")
    print("Хотите ещё что то дешифровать? (Напишите \"да\" или \"нет\")")
    if input().lower() == "да":
        continue
    else:
        break
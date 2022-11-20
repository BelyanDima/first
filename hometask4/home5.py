list = [15, 48, 'hello', 6, 19, 'world']
for i in range(6):                                # проверяем элементы списка
    f = str(list[i])
    if f.isdigit():                               # если элемент состоит из цифр
        if list[i] % 2 == 0:
            a = 0
            for x in range(0, len(f)):
                a += int(f[x])
            print('число', list[i], ' чётное, ', 'Сумма цифр=' , a)
        else:
            print('Число ', list[i], ' нечётное, список изменён')
            list[i] = list[1]
    if f.isalpha():                               # если элемент состоит из букв
        gl = 'aeiouy'                             #  создана строка из гласных букв латинского алфавита
        f.lower()
        g = 0
        s = 0
        for y in range(0, len(f)):                # проверяем буквы элемента
            for j in range(0 , 6):
                if gl[j] == f[y]:
                    g += 1
            s = len(f) - g
        print(list[i], 'количество гласных букв: ', g, 'количество согласных букв:', s)
print('Изменённый список:', list)

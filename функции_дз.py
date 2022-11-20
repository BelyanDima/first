# Задача 1 простейший калькулятор
# def calc():
#     while True:
#         a = int(input('Введите первое число: '))
#         b = int(input('Введите второе число: '))
#         c = input('Введите знак операции (+,-,*,/):')
#         if c == '+':
#             print(a, '+', b, '=', a + b)
#         elif c == '-':
#             print(a, '-', b, '=', a - b)
#         elif c == '*':
#             print(a, '*', b, '=', a * b)
#         elif c == '/':
#             try:
#                 print(a, '/', b, '=', a / b)
#             except ZeroDivisionError:
#                 print('Деление на ноль!!!')
#             finally:
#                 print('Завершение программы')
#                 break
# calc()

# Задача 2
def cort():
    a = []
    while True:
        i = input('Введите элемент кортежа (' ' завершает ввод): ')
        if i == ' ':
            break
        a.append(i)
    b = tuple(a)
    print(b)
    ds = 0
    for c in b:
        if c.isalpha():
            print(c, 'длина: ', len(c))
            ds += len(c)
    print('Общая длина слов кортежа:', ds)
def lst():
    a = []
    while True:
        i = input('Введите элемент списка (' ' завершает ввод): ')
        if i == ' ':
            break
        a.append(i)
    print(a)
    alpha = 0
    digit = 0
    for c in a:
        for b in c:
            if b.isdigit():
                digit += 1
            elif b.isalpha():
                alpha += 1
    print('Количество букв в списке: ', alpha)
    print('Количество цифр в списке: ', digit)
def ch():
    a = int(input('Введите число: '))
    b = str(a)
    nech = 0
    for i in b:
        if int(i) % 2 != 0:
            nech += 1
    print('Количество нечётных цифр: ', nech)
def st():
    a = input('Введите строку: ')
    buk = 0
    for i in a:
        if i.isalpha():
            buk += 1
    print('Количество букв в строке: ', buk)
d = input('Введите тип входящих данных (кортеж, список, число, строка): ')
if d == 'строка':
    st()
elif d == 'кортеж':
    cort()
elif d == 'список':
    lst()
elif d == 'число':
    ch()

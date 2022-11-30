#Задача 1 простейший калькулятор
# def calc():
#     while True:
#         a = int(input('Введите первое число: '))
#         b = int(input('Введите второе число: '))
#         c = input('Введите знак операции (+,-,*,/), 0 завершает программу: ')
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
#         elif int(c) == 0:
#             print('Завершение программы! ')
#             break
# calc()

# Задача 2
# def cort():
#     a = []
#     while True:
#         i = input('Введите элемент кортежа (пробел завершает ввод): ')
#         if i == ' ':
#             break
#         a.append(i)
#     b = tuple(a)
#     print(b)
#     ds = 0
#     for c in b:
#         if c.isalpha():
#             print(c, 'длина: ', len(c))
#             ds += len(c)
#     print('Общая длина слов кортежа:', ds)
# def lst():
#     a = []
#     while True:
#         i = input('Введите элемент списка (пробел завершает ввод): ')
#         if i == ' ':
#             break
#         a.append(i)
#     print(a)
#     alpha = 0
#     digit = 0
#     for c in a:
#         al = 0
#         if c[-1].isdigit():
#             digit += 1
#         for b in c:
#             if b.isalpha():
#                 alpha += 1
#     print('Количество букв в списке: ', alpha)
#     print('Количество чисел в списке: ', digit)
# def ch():
#     a = abs(int(input('Введите число: ')))
#     b = str(a)
#     nech = 0
#     for i in b:
#         if int(i) % 2 != 0:
#             nech += 1
#     print('Количество нечётных цифр: ', nech)
# def st():
#     a = input('Введите строку: ')
#     buk = 0
#     for i in a:
#         if i.isalpha():
#             buk += 1
#     print('Количество букв в строке: ', buk)
# d = int(input('Введите тип входящих данных (1 - кортеж, 2 - список, 3 - число, 4- строка): '))
# if d == 4:
#     st()
# elif d == 1:
#     cort()
# elif d == 2:
#     lst()
# elif d == 3:
#     ch()

# Задача 2
# def del_from_tupel(x):
#     a = (23, 45, 67, 98, 4)
#     b = list(a)
#     if x in b:
#         b.remove(x)
#     print(a)
#     print(tuple(b))
# del_from_tupel(int(input('Введите элемент (число): ')))

# Задача 3
def likes(*args):
    for i in a:
        print(i, end=' ,')
    print(' likes this')
a = []
while True:
    b = input('')
    if b == ' ':
        break
    a.append(b)

likes(tuple(a))




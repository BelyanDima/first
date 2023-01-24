# def factorial(n):
#     if n != 0:
#         return n * factorial(n-1)
#     else:
#         return 1
#
# print(factorial(3))

# присвоение функции переменной

# def add(a, b):
#     return a + b
# variable = add(1, 2)
# print(variable)

# def func(x): return x
#
# a1 = func
# a2 = a1
# print(a2(10))

# def sq(x): return x * x
# square = sq

# анонимная функция лямбда
# product = lambda x, y: x * y
# print(product(2 , 3))
# print(type(product))

# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(2))

# декораторы
# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# @simple_decore
# def first_test():
#     print('Test function 1')
#
# @simple_decore
# def s_test():
#     print('sfd')
#
# first_test()
# s_test()

# def raz(a):
#     return len(str(a))
#
# print('Количество разрядов: ', raz(abs(int(input('Введите число: ')))))

# def ms():
#     import random
#     a = int(input('Введите начало диапазона: '))
#     b = int(input('Введите конец диапазона: '))
#     ms1 = []
#     for i in range(10):
#         ms1.append(random.randint(a , b))
#     print(ms1)
# ms()

# # Задача 4
# def timer(x):
#     day = x // 86400
#     sec = x % 86400
#     hour = sec // 3600
#     sec1 = sec % 3600
#     min = sec1 // 60
#     sec = sec1 % 60
#
#     print('дн/час/мин/сек  :   ',day , ':', hour, ':', min, ':', sec)
# timer(int(input('Введите секунды: ')))

# Задача 5
# def gs(st):
#     gl = 'ауоыэеёиюя'
#     g = 0
#     s = 0
#     for i in st:
#         if i.isalpha():
#             if i in gl:
#                 g += 1        # Считаем гласные
#             else:
#                 s += 1
#     print('Количество гласных букв ', g)
#     print('Количество согласных букв ', s)
#
# gs(input('Введите строку: '))

# Задача 6
# def fn(n):
#     return n + (n * n) + (n * n * n)
# print(fn(int(input('Введите число: '))))

#







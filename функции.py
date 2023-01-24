# def a_function():
#     print('You just created a function!')
# a_function()
# a_function()

# def empty_function():
#     pass

# def summa():
#     a = [1, 2, 3, 4, 5, 65, 23 ,45 ,56]
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)
# summa()

# def add(a, b):
#     return a + b , a * b , a / b
#
# print(add(1, 2))
# print(add(34, 45))

# def add(a, b):
#     return a + b
#
# print(add(a=2, b=3))
#
# total = add(b=4, a=5)
# print(total)

# def keyword_function(a=1, b=2):
#     return a + b, a * b, a / b
# print(keyword_function(b=4, a=5))
# print(keyword_function())

# def mixed_function(a, b = 2, c= 3):
#     return a + b + c
#
# # mixed_function(b=4, c=5)    отсутствует аргумент a
#
# print(mixed_function(1,b=4,c=5))
# print(mixed_function(1))

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# many(1,2,3,4, name='mike', job='programmer')

# def function_a():
#     global a
#     a=1
#     b=2
#     return a + b
# def function_b():
#     c = 3
#     return a + c
#
# print(function_a())
# print(function_b())

# def sguare():
#     a = int(input('Введите сторону квадрата:'))
#     return 4 * a, a ** 2, 2**(0.5) * a
# # print(sguare())

# def season():
#     a = int(input('Введите номер месяца (1-12): '))
#     if a == 12 or a < 3:
#         print('Зима')
#     elif a >= 3 and a < 6:
#         print('Весна')
#     elif a >= 6 and a < 9:
#         print('Лето')
#     else:
#         print('Осень')
# season()

# задача 6
# def mfn():
#     import random
#     a = [random.randint(0, 1000)for i in range(10)]
#     print(a)
#     print('Среднее арифметическое элементов списка: ', sum(a) / 10)
# mfn()






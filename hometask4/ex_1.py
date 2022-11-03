 # задача 1 используя стандартные арифметические операции представьте самое большое целое число из цифр 4, 4, 4
# print(4 ** 4 ** 4)

# задача 2 : написать программу для вычисления значения выражений. проверить правильность выполнения задачи с помощью тестовых знычений
# a = int(input('введите a: '))
# import math
# y = math.pow((1 + a + (a**2)) / (2 * a + (a**2)) + 2 - ((1 - a + (a**2)) / (2 * a - (a**2))), -1) * (5 - (2 * (a**2)))
# print('y= ', y)

# a = int(input('введите a, рад:'))
# b = int(input('введите b, рад:'))
# y = int(input('введите y, рад:'))
# import math
# c = 1 / 4 * math.fabs((math.sin(a + b - y)) + math.sin(b + y - a) + math.sin(y + a - b) - math.sin(a + b + y))
# print('Y= ', c)

# # задача 3
# a = ""
# print(bool(a))       # непустая строка вернёт True

# # задача 4
# m = 10
# n = 25
# for i in range(m, n + 1):
#     print(i)

# # задача 5
# m = int(input('введите m:'))
# n = int(input('введите n'))
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m,n - 1, -1):
#         print(i)

# # задача 6
# s = 'Вася Сидоров'
# a = s.split(' ')
# print(a[1] + " " + a[0])

# # задача 7
# import random
# c = [random.randint(1, 50) for i in range(20)]
# print(c)

# # задача 8
c = [1, 5, 2, 9, 2, 9, 1]
for i in range(0, len(c)):
    if c.count(c[i]) < 2:
        print(c[i])










# # задача 9
# c = ['student1', 'student2', 'student3']
# for i in range(0,3):
#     c[i] += '_good'
# print(c)

# # задача 10
# for i in range(0,51):
#     if i == 35:
#         continue
#     print(i)

# # задача 11
# c = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
# d = []
# for i in range(0, len(c)):
#     c[i] += ' '
#     d.append(c[i])
# print(d)






# Задача 1
# import os
# os.mkdir('C:/Users/user/Desktop/PAPka')
# a = open('C:/Users/user/Desktop/PAPka/test_1.txt', 'w')
# b = open('C:/Users/user/Desktop/PAPka/test_2.txt', 'w')
# c = open('C:/Users/user/Desktop/PAPka/test_3.txt', 'w')
# os.rename('C:/Users/user/Desktop/PAPka/test_1.txt','C:/Users/user/Desktop/PAPka/rename_1.txt')
# os.rename('C:/Users/user/Desktop/PAPka/test_2.txt','C:/Users/user/Desktop/PAPka/rename_2.txt')
# os.rename('C:/Users/user/Desktop/PAPka/test_3.txt','C:/Users/user/Desktop/PAPka/rename_3.txt')
# os.remove('C:/Users/user/Desktop/PAPka/rename_1.txt')
# os.remove('C:/Users/user/Desktop/PAPka/rename_2.txt')
# os.remove('C:/Users/user/Desktop/PAPka/rename_3.txt')
# os.rmdir('C:/Users/user/Desktop/PAPka')

# Задача 2
# s = []
# sum = 0
# while True:
#     a = int(input('Введите элементы списка, при значении 999 ввод прекращается'))
#     if a == 999:
#         break
#     s.append(a)
#     sum += a
# ms = []
# for i in s:
#     if i < (sum / len(s)):
#         ms.append(i)
# print('Список:', s)
# print('Среднее арифметическое по списку:', sum / len(s))
# print('Список элементов, значение которых ниже среднего арифметического:', ms)

# Задача 3
# a = {1, 2, 3, 4, 5, 6, 7}
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# if a == b:
#     print('Множества равны')
# if len(a) == len(a.union(b)):
#     print('Множество 1 состоит из множества 2')
# if len(b) == len(a.union(b)):
#     print('Множество 2 состоит из множества 1')
# c = a & b
# if len(c) == 0:
#     print('Множества не пересекаются')
# else:
#     print('Множества пересекаются, пересечение:', c)

# Задача 4
# s = 'An apple a day keeps the doctor away'
# d = {i: s.count(i) for i in s}
# print(d)

# Задача 5
# mn = set()
# for i in range(10):
#     mn.add(int(input('Введите элемент: ')))
# print(mn)

# Задача 6
# sd = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
# sum = 0
# b5 = []
# s1 = {}
# for t in sd:
#     sum += sd.get(t)
#     if sd.get(t) > 5:
#         b5.append(t)
#     tsp = t.split(' ')
#     if len(tsp) == 1:
#         s1[t] = sd.get(t)
# print('Общее время звучания песен: ', sum)
# print('Список песен, время звучания которых больше 5 минут:', b5)
# print('Названия песен из одного слова: ', s1)

# Задача 7
# s = input('Введите строку:')
# s1 = []
# for i in s:
#     if i not in s1:
#         s1.append(i)
# print('Первые вхождения символов: ', tuple(s1))

# Задача 8
# arr = []
# while True:
#     ar = int(input('Введите элементы массива, 999 завершает ввод: '))
#     if ar == 999:
#         break
#     arr.append(ar)
# arr1 = []
# a = int(input('Введите нижнюю границу интервала: '))
# b = int(input('Введите верхнюю границу интервала: '))
# for i in arr:
#     if i < a or i > b:
#         arr1.append(i)
# for i in range(len(arr) - len(arr1)):
#     arr1.append(0)
# print('Исходный массив: ', arr)
# print('Массив в заданных параметрах: ', arr1)

# Задача 9
i = int(input('Введите количество строк матрицы: '))
j = int(input('Введите количество столбцов матрицы: '))
print('Создаём матрицу: ')
matrix = []
for a in range(j):
    m1 = []
    for b in range(i):
        print('Создаём строку', a + 1)
        b1 = int(input('Введите элемент :'))
        m1.append(b1)
    matrix.append(m1)
print(matrix)
sum = 0
for a in range(1, i):
    for b in range(0, a):
        if matrix[a][b] < 0:
            sum += 1
print('Количество отрицательных элементов под главной диагональю матрицы: ', sum)




# Задача 10
# ar = []
# sum = 0
# while True:
#     a = int(input('Введите элементы, при значении 999 ввод прекратится:'))
#     if a == 999:
#         break
#     ar.append(a)
# b = int(input('Введите нижний предел: '))
# c = int(input('Введите верхний предел: '))
# for i in ar:
#     if i > b and i < c:
#         sum += i
# print('Сумма элементов в указанном интервале (не включая граничные значения): ', sum)

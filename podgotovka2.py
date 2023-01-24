# Задача 1 создать папку на рабочем столе при помощи os
# import os
# os.mkdir('C:/Users/user/Desktop/papka')

# Задача 2 удалить созданную папку c помощью os
# import os
# os.rmdir('C:/Users/user/Desktop/papka')

 # Задача 3 создать файл
# f = open('C:/Users/user/Desktop/task_1.txt', 'w')
# import os
# os.rename('C:/Users/user/Desktop/task_1.txt','C:/Users/user/Desktop/renamefile.txt')

# Задача 4
# s = 'hellomynameis'
# d = {i: s.count(i) for i in s}
# print(d)

# Задача 6
a = [1,7,7,5,4,3,7,9]
b = [2,5,3,4,6,7,8,5]
c = []
for i in a:
    if i in b:
        c.append(i)
print('Элементы, содержащиеся в обоих списках:', *c, sep=' ')
print('Количество элементов, содержащихся в обоих списках:', len(c))

# Задача 5
# a = [1, 2, 3, 4, 5]
# b = ['one','two','three','four','five']
# print(dict(zip(a,b)))

# Задача 7

# a = [i for i in range(1, 51)]
# print(tuple(a))

# Задача 8

# a = {'first': 56,'second': 39,'therd': 67}
# mn = 1
# for i in a:
#     mn *= a[i]
# print('mn= ', mn)

# Задача 9
# a = [56, 34, 78, 12, 34, 12]
# a.sort()
# print('наименьшие элементы: ', a[0], a[1])

# Задача 10
# s = 0
# a = [-5, 8, 9, 16, -7, 25, 32]
# for i in a:
#     if i % 2 == 0 and i > 0:
#         s += i
# print('Сумма чётных положительных элементов списка:', s)

# # Задача 11
# a = int(input('Введите количество первых элементов ряда Фибонначи:'))
# s = [0, 1]
# for i in range(2, a):
#     s.append(s[i-1] + s[i-2])
# print(*s, sep=' ')








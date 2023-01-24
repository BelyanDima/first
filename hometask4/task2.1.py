# a = (1, 2, 3, 4, 5, 6, 7)
# b = [1, 2, 3, 4, 5, 6, 7]
# print(a.__sizeof__())

# a = (1, 2, 3, 4, 5, 6)
# print(a[0:3])
# print(a[:3])
# print(a[1:])
# print(a[2::2])
# print(a[::2])

# a = (10, 2.13, "squre", 89, 'C')
# b = [1, 2, 3]
# c = list(a)
# d = tuple(b)
# print(c)
# print(d)

# nested = (1, "do", ["param", 10 ,20])
# nested[2][1] = 15
# print(nested)

# x = (1, 2, 3, 4)
# z = x * 2
# print(z)

# a = 1,
# print(type(a))

# a = (1, 2, 3, 4, 5, 5)
# print('max ', max(a), 'min ', min(a))

# import random
# a = []
# i = 0
# while i < 10:
#     a.append(random.randint(0 , 100))
#     i += 1
# a = tuple(a)
# print(a)
# print('max=', max(a), 'min =', min(a))

# import random
# a = []
# b = []
# for i in range(10):
#     a.append(random.randint(0 , 5))
# for i in range(10):
#     b.append(random.randint(-5 , 0))
# a = tuple(a)
# b = tuple(b)
# c = a + b
# print(c , ' количество нулей:',c.count(0))

# a = ( 'one','two','three','four')
# c = (','.join(a))
# print(str(c))

# A = (13,5,43,49,67,32,12,98,6,10,34,20,55,68,14,60,14)
# B = (53,21,4,23,76,3,43,12,54,342,21)
# if sum(A) > sum(B):
#     print('Cумма больше в кортеже A')
# else:
#     print('Cумма больше в кортеже B')
# print('индекс мин A: ',A.index(min(A)) +1)
# print('индекс мин B: ',B.index(min(B)) + 1)

# ЗАКРЕПЛЕНИЕ ТЕМЫ
# A = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(sum(A))

# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'т', 'и')
# print('Статистика частности букв в кортеже:')
# print('т - ', long_word.count('т'))
# print('а - ', long_word.count('а'))
# print('и - ', long_word.count('и'))

# week_temp =(26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))

a = [4, 6, 'py', 'exept', 78]
b = [44, 'hello', 56, 'exept', 3]
c = a + b
c.insert(3, 6)
print('суммарный список c:', c)
for i in c:
    if type(i) is str:
        c.remove(i)
print('итоговый список c:', c)
print('количество элементов итогового списка', len(c))












# a = input('Введите текст:')
# print(a[2])
# print(a[-2])
# print(a[0:5])
# print(a[:-3])
# print(a[::2])
# print(a[1::2])
# print(a[-1::-2])
# print(len(a))
# for i in range(4):
#     print(i)
# for i in range(4, 8, 1):
#     print(i)
# for i  in range(1 , 9, 3):
#     print(i)
# for i in range(20 , 1, -3):
#     print(i)
# for i in "Я УЧУ PYTHON":
#     print(i)
# a = input("введите строку:")
# b = input("введите символ:")
# c = " "
# for i in a:
#     if i != b:
#         c += i
# print(c)
# a = int(input("введите начало последовательности:"))
# b = int( input("введите конец:"))
# c = int(input("введите шаг"))
# for i in range(a, b, c):
#     print(i)
# for i in range(54, 9184):
#     if i % 5 == 0:
#         print(i)
# arr = ['string1', 'string2', 'string3']
# l = len(arr)
# print(arr , 'длинна:', l)
# arr = [1,7,9,10]
# for i in arr:
#     print(i)
# arr = [1, 7, 9 , 10]
# for i in arr:
#     print(i)
#     if i == 9:
#         break
# arr = [1,7,9,10]
# for i in arr:
#     if i == 9:
#         continue
#     print(i)
# a = [10, 2, 3]
# print(a)
# a.append(7)
# print(a)
# a = [1,2,5,3,2,5,78]
# s = 0
# pr = 1
# for i in a:
#     s += i
#     pr *= i
# print('s=', s)
# print('pr=', pr)
# a = input('Введите строку:')
# b = ""
# for i in a:
#     if i != " ":
#         b += i
# print(b)
# if b == b[::-1]:
#     print('перевёртыш!')
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1
# i = 0
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1
# i = 1
# result = 0
# while i <= 50:
#     result += i
#     i += 1
# # print(result)
# i = 1
# while i <= 10:
#     print(i **2)
#     i = i + 1
# i = 15
# while i >= 1:
#     print(i)
#     i -= 1
# a = int(input('введите первое число'))
# b = int(input('введите второе число'))
# a += 1
# while a <= b:
#     if a < 0:
#         print(a)
#     a = a + 1
# a = int(input())
# b= int(input())
# while a < b - 1:
#     a += 1
#     if a == 0:
#         break
#     print(a)
# for i in range(5):
#     print(i)
# else:
#     print('готово!')

# i = 0
# while i < 3:
#     print(i)
#     i+=1
# else:
#     print(' готово')
# arr = []
# i = 7
# while i <= 98:
#     arr.append(i)
#     i += 7
# print(arr)
# print(len(arr))
# while True:
#     a = float(input('введите первое число'))
#     b = float(input('введите второе число'))
#     c = input('введите знак')
#     if c== '/' and b == 0:
#         print('деление на ноль!!!')
#         break
#     if c== '+':
#         print('a+b=',a + b)
#     elif c== '-':
#         print('a-b=',a - b)
#     elif c=='*':
#         print('a*b',a * b)
#     elif c=='/':
#         print('a/b=',a/b)
# задача №1
# pr = 1
# for i in range(1 , 100 , 2):
#     pr *= i
# print('Произведение нечётных чисел от 1 до 100 pr=', pr)
# Задача №2
# arr = []
# for i in range(1 , 501):
#     if i % 5 == 0:
#         arr.append(i)
# print('arr=', arr)
# print('Всего элементов массива:', len(arr))

# # Задача №3
# for i in range( 1, 498):
#     if i % 2 == 0:
#         print(i)

# Задача №4
# arr = [2,4,55,6,2,9,6,2,4,5,5,5,9,9]
# povtor = []
# for i in range(0, len(arr)-1):
#     for a in range(i + 1 , len(arr)):
#         if arr[i] == arr[a]:
#             for b in range(a + 1, len(arr)):
#                 if arr[i] == arr[b]:
#                     povtor.append(arr[i])
#                     break
# print("Исходный список:", arr)
# print("Список элементов, встречающихся более двух раз:", povtor)

# arr = [2,4,55,6,2,9,6,2,5,5,5,9,9]
# povtor = []
# for i in range(0, len(arr)):
#     if arr.count(arr[i]) >= 3:
#         povtor.append(arr[i])
# print(arr)
# print(povtor)

# for i in range(1, 10):
#     for x in range(1 , 10):
#         print(f'{i * x:3}' , ' ', end= " ")
#     print()
# elements = list()
# print(elements)
# import random
# c = [random.randint(0 , 100) for i in range(10)]
# print(c)
# elements = [1, 2, 4, 5]
# elements.insert(2, 3)
# print(elements)
# elements = [1,3,3,4,5]
# elements[1]= 2
# print(elements)
# elements = [1 ,3 , 'a', 6, 'a', 'b']
# del elements[3]
# elements.remove('a')
# print(elements)
# my_list = ['hello', 'world']
# elements = [1, 3 , my_list, 6, 'a', 'b']
# del elements[2][1]
# print(my_list, elements)
# d = ['h', 'e', 'l', 'l', 'o']
# e = ['w', 'o', 'r', 'l', 'd']
# d.extend(e)
# print(d)

# # copy
# a = [1, 2, 3]
# b = a.copy()
# print(id(a), id(b), a, b)

# index
# elements = ['one', 'two', 'thre', 'one']
# print(elements.index('thre'))

# elements = [['яблоки', 50], ["апельсины", 190]]
# print(elements[1])

# arr = [3, 4 , 5 ,7]
# arr.reverse()
# print(arr)
# sp = [1, 4 ,5, 20, 10,2]
# sp[sp.index(20)] = 200
# print(sp)

# sp = [1, 2, 3 , 4 , 5, 6, 7]
# nech = 0
# ch = 0
# s = 0
# pr = 1
# for i in range(0 , 7):
#     if sp[i] % 2 == 0:
#         ch += 1
#     else:
#         nech += 1
# if ch > nech:
#     for i in range(0 , 7):
#         s += sp[i]
#     print('сумма всех цифр:',s)
# if ch < nech:
#     print("произведение 1, 3, 6элементов=", sp[1]* sp[3] * sp[6])

# import random
# while True:
#     print('Рады приветствовать Вас в казино "ФОНТАН УДАЧИ"!!!')
#     a , b = int(input('Выберите число от 1 до 10:')), input('Выберите цвет: красный, чёрный:')
#     x = random.randint(1 , 10)
#     y = random.randint(1,2)
#     if y == 1:
#         c = "красный"
#     else:
#         c = "чёрный"
#
#     if a == x and b == c:
#         print('УДАЧА УЛЫБНУЛАСЬ ВАМ!!! Распределяем выигрыш по карманам, делаем новую ставку')
#     else:
#         print('Вы почти угадали, стоит попытаться ещё, удача рядом!!!')
#         print('Правильная ставка:', x, ';' , 'цвет:', c)

# x = int(input('введите x:'))
# y = int(input('ведите y:'))
# print((abs(x)- abs(y)) / (1 + abs(x * y)))
# import math
# a = int(input('введите значение первого катета:'))
# b = int(input('введите значение второго катета:'))
# print('гипотенуза треугольника :', math.sqrt(a**2 + b**2))
# print(' площадь треугольника :', a* b* 0.5)

# a = 9
# b = 17
# c = 5
# if a > b:
#     print( 'a > b')
# else:
#     print('a <= b')
# if a== b - c:
#     print('a = b-c')
# else:
#     print('a!=b-c')
# if b == a + c:
#     print('b=a+c')
# else:
#     print('b!=a+c')
# if c <= a + b:
#     print('c<=a+b')
# else:
#     print('c>a+b')
# if a < b and a > c:
#     print('a<b, a>c')
# else:
#     print('a>=b,a<=c')
# if b > a or b > c:
#     print('b>a, or b>c')
# else:
#     print('b<=a or b<=c')

# str = "Robin Sight"
# arr =[]
# arr.append(str[:5])
# arr.append(str[-5:])
# print(arr)

# str = "I love arrays they are my favorite"
# str_1 =str.split(" ")
# str_1[2] = "lists"
# print(str_1)

# arr = ['I','love','lists','they','are','my','favorite']
# str = ""
# for i in range(0 , 7):
#     str = str + arr[i] + " "
# print(str)

# a = [-8, 1, 2, -2, 0]
# b = [1, -1, 0, -9, 4, -5]
# c = [1, 4, 0, 23, 6, 34]
# a.sort()
# b.sort()
# c.sort()
# print('', a[1])
# print('', b[1])
# print('', c[1])

# c = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# d = []
# d.append(c[0])
# d.append(c[4])
# d.append(c[5])
# print(c)
# print(d)

# m = int(input('введите m: '))
# n = int(input('введите n: '))
# if m < n:
#     for i in range(m , n + 1):
#         print(i)
# else:
#     for i in range(n , m + 1):
#         print(i)

# i = 0
# while i <=3:
#     a = int(input(' решите пример 3+4*2=: '))
#     if a == 11:
#         print('правильно!')
#         break
#     else:
#         print('АШЫПКА!!!, осталось попыток:', 3 - i)
#     i += 1
# else:
#     print('бесплатные попытки закончились!')

list = [1,4,20,13,22,20,43,34,20,12,14,12,20]
for i in range(0 , len(list)):
    if list[i] == 20:
        del list[i]
print(list)






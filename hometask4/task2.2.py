# d = {}
# d = {'dict': 1, 'dictionary': 2}
# print(d)

# d = dict(short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])
# print(d, '\n', d_2)

# d = dict.fromkeys(['a','b'])
# d_2 = dict.fromkeys(['a','b'], 100)
# print(d,'\n', d_2)

# d = {a: a** 2 for a in range(7)}
# print(d)

# d = {1: 2, 2: 4, 3: 9}
# d[4] = 4 ** 2
# d[7] = 49
# d[6] = 36
# d[2] = 5
# print(d[1])
# print(d)

# Mounth = {1: 'Jan', 2:'Feb', 3: 'Mar'}
# count = len(Mounth)
# print(count)
# for mn in Mounth:
#     print(mn,':', Mounth[mn])

# Salary = {'Director': 120800.0, 'Secretary': 101150.25, 'Locksmith': 188200.00}
# print(Salary)
# del Salary['Secretary']
# print(Salary)
# удалить элемент по ключу 'Secretary' с проверкой
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)
# # попытка удалить несуществующий ключ
# key2 = 5
# if key2 in Salary:
#     del Salary[key2]

# Position = {'Manager':{'Director', 'Deputy Director'}, 'Teacher': {'Specialist','Methodist','Senior Lecturer'}, 'Staff': {'Cleaner', 'Porter', 'Watchman'}}
# count1 = len(Position)
# count2 = len(Position['Manager'])
# count3 = len(Position['Staff'])
# print(count1)
# print(count2)
# print(count3)

# Numbers = dict(zip([1,2,3],['One','Two','Three']))
# print(Numbers)

# Задача 1
# person = {'name' :('Иван', 'Марина', 'Ольга'),'age': (19 , 23, 25), 'city': ('Minsk', 'Gomel', 'Grodno')}
# print(person['age'])

# Задача 2
# m = { 'BMW': ['i7', 'i4', 'Concept XM'], 'Tesla': ['Roadster', 'Semy' , 'Model X']}
# print(m['BMW'][0], m['BMW'][2], m['Tesla'][0], m['Tesla'][2])

# Задача 3
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(d1['b'] == d2['b'])

# Задача 4
# dolgi = {'Vasya': 45, 'Petya': 65, 'Sanya': 114}
# proizv = 1
# for i in dolgi:
#     proizv *= dolgi[i]
# print(proizv)

# Задача 5
# a = ['one', 'two', 'three']
# b = [1, 2, 3]
# d = dict(zip(a, b))
# print(d)

# Задача 6
s = 'pythonlist'
d = {i: s.count(i) for i in s}
print(d)


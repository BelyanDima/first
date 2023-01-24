# string_set = {'Nicolas', 'Mishelle','john', 'Mercy'}
# print(string_set)

# mixed_set = {2.0 , "Nicholas", (1, 2, 3)}
# print(mixed_set)

# num_set = set([1, 2, 3, 1, 2])
# print(num_set)

# num_set = {1, 2, 3, 2, 1}
# print(num_set)

# x = {}
# print(type(x))

# x = set()
# print(type(x))

# mounth = set(['Jan', 'Feb', 'march', 'Apr'])
# for i in mounth:
#     print(i)
# print("Feb" in mounth)

# mounth = set(['Jan', 'Feb'])
# mounth.add('March')
# print(mounth)

# num_set = {1, 2, 3, 4, 5, 6}
# # num_set.discard(3)
# # num_set.remove(3)
# # num_set.pop()
# num_set.clear()
# print(num_set)

# mounth_a = set(['Jan', 'Feb' , 'March'])
# mounth_b = set(['July', 'Aug'])
# mounth = mounth_a.union(mounth_b)
# print(mounth)

# x = {1, 2, 3}
# y = {4, 3, 6}
# z = {7, 4, 9}
# # output = x.union(y , z)
# # print(output)
# print(x| y| z)

# x = {1, 2, 3}
# y = {4 , 3, 6}
# print(x & y)

# A = {1, 2, 3}
# B = {4, 3, 6}
# print(A - B)
# print(B - A)

# Задача 1 проверить, есть ли в числовой последовательности дубликаты
# a = (1, 2, 3, 5, 6, 7)
# b = set(a)
# if len(a) == len(b):
#     print('False')
# else:
#     print('True')

# Задача 2
# a = {1 : "one" , 2 : "two", 3 : "three"}
# a["four"] = 4
# a[(5, 6, 7)] = ['five', 'six', 'seven']
# print(a)
# print(a[2])
# del a[3]
# print(a)
# print(a.keys())

# Задача 3
a = set([1, 3, 5, 4, 2])
b = frozenset([7, 8, 9, 6, 5, 4])
print(a | b)
print(a & b)
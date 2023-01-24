# f = open('Blok.txt', 'r') # открыть текстовый файл в режиме чтения
# # print(*f) # выводим содержимое файла
# # print(f) # выводим объект
# # print(f.read(7))
# # print(f.read(7))
# # print(f.readline())
# print(f.readlines(2))

# f = open('xyz.txt', 'w')   #открытие в режиме записи
# f.write('Hello \nWorld')   #запись Hello World в файл
# f.close()                  # закрытие файла

# import os
# print('Текущая директория', os.getcwd())
# os.mkdir('folder')       # создать пустой каталог (папку)
# import os
# # os.chdir('folder')
# # print('текущая директория-', os.getcwd())
# # os.chdir('..')
# # os.makedirs('dim1/dim2/dim3')
# # os.remove('abc.txt')
# os.rmdir('folder')

# with open('Blok.txt', 'r') as f:
#     a = f.readlines()
#     print(a)
# for i in a:
#     i = i.replace('_', ' ')
#     l = i.split(' ')
# print(l)
# s = 0
# for i in l:
#     if i.isdigit():
#         s += int(i)
# print(s)

s = []
b = []
c = []
while True:
    a = input()
    if a == '':
        break
    s.append(a)
f = open('C:/Users/user/Desktop/blokNote.txt', 'w')
for i in s:
    if i.isalpha():
        b.append(i)
    else:
        c.append(int(i))
for n in range(len(b)):
    f.write(max(b, key=len))
    f.write('\n')
    b.remove(max(b, key=len))
c.sort()
for i in c:
    f.write(str(i))
    f.write('\n')





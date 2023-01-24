# Задача 1
sklad = {'Наименование' : ['Цена' , 'Количество'], 'Ручка': [2, 170], 'Карандаш' : [1.5, 400], 'Ластик': [3, 45]}
for i in sklad:
    print(i, sklad[i][0], sklad[i][1], sep='-')
sum = 0
while True:
    name = input('Введите название товара: ')

    if name == 'n':
        break
    else:
        amount = int(input('Введите количество: '))
        if name in sklad:
            sum += sklad[name][0] * amount
            sklad[name][1] -= amount
        elif sklad[name][1] - amount < 0:
            print('Недостаточно товара на складе')
print('Сумма к оплате:', sum)
print('Остатки на складе: ')
for b in sklad:
    print(b, sklad[b][0],sklad[b][1], sep = '-')



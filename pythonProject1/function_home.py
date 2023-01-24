def calculator(a, b, c):
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '/':
        try:
            return a / c
        except ZeroDivisionError:
            print('Деление на ноль!!!')

while True:

    a = int(input('Введите первое число (9999 останавливает процесс): '))
    b = input('Ведите знак операции (+,-,*,/): ')
    c = int(input('Введите второе число: '))
    if a == 9999:
        break
    print(calculator(a, b, c))
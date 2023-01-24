# # создание класса
# class Human:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#
#     def walk(self, km):
#         if km > 5:
#             return f'Я не могу пройти {km} км'
#         else:
#             return f'Я могу пройти {km} км'
#
#
# # создание обьекта
# my_human = Human('artem', 19)
#
# class Car:
#     # статические поля (переменные класса)
#     default_color = 'Grey'
#     default_weight = 5000
#
# def __init__(self, color, model):
#     # динамические поля(переменнные объекта)
#     self.color = color
#     self.model = model
#
# def turn_on(self):
#     pass
# print(dir(Car))

# class Example:
#     a = 7
#     b = 5
#
#     def __init__(self, t , r):
#         self.t = t
#         self.r = r
#
#     def func(self):
#         self.c = 4
#         print(self.c)
#
#     def func1(self):
#         return self.a + self.b
#
#     def func2(self):
#         return self.t ** self.r
#
# example = Example(4, 2)
# print(example.a)
# print(example.func1())
# print(example.func2())
# example.func()

class Calc:

    def __init__(self):
        self.input()

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def input(self):
        self.a = float(input('Введите первое число: '))
        self.b = float(input('Введите второе число: '))



while True:

    calc = Calc()
    c = input('Введите операцию( +, -, *, /): ')
    if c == '+':
        print(calc.plus())
    elif c == '-':
        print(calc.minus())
    elif c == '*':
        print(calc.mult())
    elif c == '/':
        print(calc.div())
    else:
        break

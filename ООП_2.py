# class Car:
#
#     # создание методов класса
#     def __str__(self):
#         return 'Car class Object'
#
#     def start(self):
#         print('Двигатель заведён')
#
# car_a = Car()
# print(car_a)

# Статический метод
# class Phone:
#
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
# Phone.model_hash('I785')
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')
# print(Phone.model_hash('I785'))

# class Human:
#     default_name = 'Vasya'
#     default_age = 25
#
#     def __init__(self, name = default_name, age = default_age):
#         self.name = name
#         self.age = age
#         self.__money = 1250
#         self.__house = 'flat'
#
#     def info(self):
#         print(self.name)
#         print(self.age)
#         print(self.__money)
#         print(self.__house)
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#
#     def earn_money(self, upmoney):
#         self.__money += upmoney
#         print(f'upmoney: {upmoney}, money: {self.__money}')
#
# # Тесты
# Human.default_info()
# Pasha = Human('Pasha', 27)
# Pasha.info()
# Pasha.earn_money(1000)
# Pasha.info()

import string

class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):


    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    __letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, a):
        a = input('Введите букву: ')
        if a.upper() in self.letters:
            print(f'Буква {a} относится к английскому алфавиту')
        else:
            print(f'Буква {a} не относится к английскому алфавиту')

    def letters_num(self):
        return EngAlphabet.__letters_num
    @staticmethod
    def example():
        return f'To be, or not to be?'

en_alphabet = EngAlphabet()
en_alphabet.print()


# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 1
# print(k)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['d']
# except KeyError:
#     print('ключа не существует!')
# except IndexError:
#     print('такого индекса нет')
# # except:
# #     print('произошла другая ошибка')
# # except (IndexError, KeyError):
# #     print('Произошла ошибка IndexError или KeyError')
#
# else:
#     print('Oшибок не произошло!')
# finally:
#     print('Оператор finally выполнен!')

# # задача 1
# a = int(input("введите первое число : "))
# b = int(input("введите второе число: "))
# try:
#     c = a / b
# except ZeroDivisionError:
#     c = 0
# else:
#     c = c**2
# print(c)
# finally:


# # Задача 2
# a = int(input('введите первое число '))
# b = int(input('введите второе число '))
# try:
#     c = a / b
# except ZeroDivisionError:
#     print('деление на ноль')
# except ValueError:
#     print('ошибка преобразования')
# except Exception:
#     print('общая ошибка')
# print(c ,  '   end!!!')




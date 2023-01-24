# def get_sum(a,b):
#     pass
#
# print(get_sum(4,2))

# def get_sum(a=2,b=3):
#     print(a+b)
#
# get_sum(4)

# class Test:
#     test = None
#
# print(Test.test)

# class Test:
#     def print_text(self):
#         print('это родительский класс')
# class Test2(Test):
#     def print_text(self):
#         print('это дочерний класс')
# test2 = Test2()
# test2.print_text()

class Test:
    __test = 0
print(Test.__test)
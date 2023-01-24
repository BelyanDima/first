# class Student:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
# student1 = Student('Petya', 100)
# student2 = Student('Kolya', 100)
# student3 = Student('Vasya', 150)
# students = [student1, student2, student3]
# moneys = []
# # for student in students:
# #     moneys.append(student.money)
# # print(moneys)
# moneys = [student1.money, student2.money , student3.money]
# print(moneys)
# if max(moneys) == min(moneys):
#     print('all')
# else:
#     max_money = 0
#     name_student = ''
#     for student in students:
#         if student.money > max_money:
#            max_money = student.money
#            name_student = student.name
#     print(f'Студент с наибольшим количеством денег {name_student}--->{max_money}')

# задача 1
# class Calculator:
#     def validate_number(self, a, b):
#         is_valid_first_number == isinstance(a, int) or isinstance(a, float)
#         is_valid_second_number == isinstance(b, int) or isinstance(b, float)
#     if is_valid_first_number and is_valid_first_number:
#         print('valid')
#     else:
#         raise Exception('Not Valid')
#     def sum(self, a , b):
#         self.validate_number(a, b)
#         return a + b
#     def dif(self, a, b):
#         self.validate_number(a, b)
#         return a - b
#     def div(self, a, b):
#         self.validate_number(a, b)
#         if b == 0:
#             print('Error!!!')
#         else:
#             return a / b
#     def mult(self,a ,b):
#         self.validate_number(a, b)
#         return a * b
#
# calc = Calculator()
# print(calc.sum(3,8))
#
# class Orange:
#
#     def __int__(self, sort , vitamins, price, name):
#         self.sort = sort
#         self.vitamins = vitamins
#         self.price = price
#         self.name = name
#
#     def clear(self):
#         return f'{self.name} is clear'
#
#     def __repr__(self):
#         return f'sort {self.sort}, vitamins {self.vitamins} , price {self.price} , name {self.name}'
#
#
# class Apple(Orange):
#
#     def cut(self):
#         return f'{self.name} is cut'
#
# class Tangerane(Orange):
#     pass
#
# class Banana(Orange):
#     def __init__(self, sort, vitamins, price, name, num_of_calium):
#         super().__init__(self,sort, vitamins, price, name)
#         self.num_of_calium = num_of_calium
#
#     def __repr__(self):
#         return f'sort {self.sort}, vitamin {self.vitamin}, price {self.price}, name {self.name}, num_of_calium {self.num_of_calium}'
#
# orange = Orange('Verna', ['a', 'b1', 'c'], 100, 'orange')
# apple = Apple('Antonovka', ['a', 'b', 'c'], 120, 'apple')
# tangerine = Tangerane('klementine', ['a', 'b', 'c'], 150,'tangerine')
# banana = Banana(')


class Student:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress
    def __repr__(self):
        return self.name

class School:

    def __init__(self,students):
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def get_list_of_students(self):
        return self.students

    def remove(self, student, group):
        if student.group == group:
            self.students.remove(student)

    def print_names(self):
        for student in self.students:
            print(student.name)

    def print_group(self, group):
        st = []
        for student in self.students:
            if student.group == group:
                st.append(student)
        return st

    def get_list_automate_students(self,automark==7):
        list_automate = []
        arifm = sum(student.progress) / len(student.progress)
        if arifm >= automark:
            list_automate.append(student)
        return list_automate

    def get_list_of_students_needed_mark(self, grades):
        self.grades= grades


student1 = Student('Petya', '1A', [5, 5, 5, 5, 5])
student2 = Student('Kolya', '1B', [8,9,7,8,9])

school = School([])

school.add_student(student1)
school.add




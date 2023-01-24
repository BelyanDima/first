# def simple_decore(fn):
#     def wrapper():
#         print('Start function')
#         fn()
#         print('Stop function')
#     return wrapper
#
# def first_test():
#     print('Test function 1')
#
# def second_test():
#     print('Test function 2')
#
# first_test_wrapped = simple_decore(first_test)
# second_test_wrapped = simple_decore(second_test)
# first_test_wrapped()
# second_test_wrapped()

def simple_decore(fn):
    def wrapper():
        print('Start function')
        fn()
        print('Stop function')
    return wrapper

@simple_decore
def first_test():
    print('Test function 1')

@simple_decore
def s_test():
    print('sfd')

first_test()
s_test()
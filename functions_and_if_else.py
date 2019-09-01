
#basic function declaration
def basic_function():
    print('This is the first function') #note indentation is necessary as there are no curly brackets

basic_function()


def function_with_return():
    return "I retrned Hello World"

print(function_with_return())


def function_wth_params(num1, num2):
    return 'Param 1 = ' + str(num1) + ' and  Param 2 = ' + str(num2)

print(function_wth_params(20, 30))


def maximum_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

maximum_of_three(20,45,10)

try:
    number = int(input ('Enter any random integer'))
    print(number/0)
except ValueError as err:
    print('Invalid input')
except ZeroDivisionError as err: #you can just print err as well
    print('Cannot Divide by Zero')
except:
    print('Any other error') #fail safe case will caught any type of error if not of above 2 types





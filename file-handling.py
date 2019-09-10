file = open('employees.txt', 'r') #read
if file.readable(): #if reaable then print file as is
    print('read entire file:')
    print(file.read())
file.close()

file = open('employees.txt', 'r') #read
if file.readable(): #if reaable then print file as is
    print('just read one line:')
    print(file.readline())  # print a line
file.close()

file = open('employees.txt', 'r') #read
if file.readable(): #if reaable then print file as is
    print('using readlines() in for')
    for line in file.readlines():
        print(line)
file.close()

file = open('employees.txt', 'a') #append
file.write('3, Manju\n')
file.close()

file = open('employees.txt', 'r') #read
if file.readable(): #if reaable then print file as is
    print('After appending Manju:')
    print(file.read())
file.close()


file = open('employees.txt', 'w') #write
file.write('1, Digender\n')
file.write('2, Hemanti\n')
file.write('4, Geeta\n')
file.close()

file = open('employees.txt', 'r') #read
if file.readable(): #if reaable then print file as is
    print('After ovverriding:')
    print(file.read())
file.close()

# file = open('employees.txt', 'r+') #read and write
# file.close()

i = 10
data = ''
while i > 0:
    print(i, end =", ")
    i-=1

print(data)
data = ''
for letter in "Hello":
    print(letter, end =" ")

print('')

friends = ['Jim', 'Carey', 'DJ']

for name in friends:
    print(name, end =",")

print('')
for num in range(10):  #0 to 9
    print(num, end =",")

print('')
for num in range(3, 10):  #4 to 9
    print(num, end =",")

#ternary

def min(num1, num2):
    print(num1 < num2)
    return (num1, num2)[num1 > num2]

print('Minumum value')
print(min(20, 10))

print('')
for num in range(len(friends)):  #using len for calculating length
    print(friends[num], end =",")

print('')

#function to calculate exponentials using for loop

def power(number, index):
    value = 1;
    for i in range(index):
        value *= number;
    return value;
print('print power')
print(power(2, 10))
print(power(5, 5))
print(power(10, 3))
print(10**5)

two_d_array = [
    ['Mango', 'Banana', 'Raspberry', 'Pineapple', 'grapes'],
    ['Lily', 'Rose', 'Shoe Flower', 'Jasmine'],
    [20, 30, 10, 50, 90, 1],
]

print('2-D array is: ')
for array in two_d_array:
    for val in array:
        print(val, end = ' ')
    print('')

#translater

def translater(text, replacer):
    translation = ''
    for letter in text:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + replacer.upper()
            else:
                translation = translation + replacer.lower()
        else:
            translation = translation + letter
    return translation
print(translater(input('Enter Input text'), input('Enter replacer')))

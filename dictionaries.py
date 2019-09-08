#this is more like a json or a map in java ;)
monthConv = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
}

print(monthConv['Jan']) #default way to get the value from key
# print(monthConv['Jan1']) #not safe will terminate the program

#safer method .get()

print(monthConv.get('Feb'))
print(monthConv.get('Jan1')) #safe will give output as None

print(monthConv.items()) #all keys and values in tuple
print(monthConv.keys()) #get all keys in list
print(monthConv.values()) #get all values in list
# monthConv.popitem('Jan');


dictionary = dict({0: 'Hello', 2: 'World', 'Jan': 'January'})
print(dictionary) #print dictionay created with dict

dictionary.pop('Jan');
print(dictionary) #print dictionay after pop


dictionary.popitem(); #removes the last element
print(dictionary) #print dictionay after pop

dictionary[5] = 'Blah' #adds new key 5 and value blah
print(dictionary)

dictionary.pop(0);# removes key 0
print(dictionary) #print dictionay after pop

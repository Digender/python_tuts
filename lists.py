#arrays and lists

fruit_list = ['Mango', 'Orange', 'Banana', 'melon', 'papaya']
flowers = ['Rose','Lily', 'Jasmine', 'Marigold', 'Shoe flower']
random_numbers = [5, 1, 100, 2, 50]

joined_array = []
copied_list = []

print('First element of fruits: ' + str(fruit_list[0]))
print('Second Last element of fruits: ' + str(fruit_list[-2]))
print('From index 1 to n: ' + str(fruit_list[1:])) #range till end
print('From index 1 to 4: ' + str(fruit_list[1:4])) #range till specified


#methods for lists

#extend() like concat and modify source

joined_array.extend(fruit_list)
joined_array.extend(flowers)
joined_array.extend(random_numbers)
print('Extended List: ' + str(joined_array))


#index() like concat and modify source

print('Index of banana in list: ' + str(joined_array.index('Banana')))

#append
fruit_list.append('Guava')
print('Add to last using append(): ' + str(fruit_list)) #add to last

#pop
fruit_list.pop()
print('Remove Last using pop(): ' + str(fruit_list)) #remove last

#insert(index, 'Element')
fruit_list.insert(1, 'Guava');
print('Add at index using insert(): ' + str(fruit_list)) #add element at index position

#remove() remove an element in list

joined_array.remove('Banana')
print('Remove banana using remove(): ' + str(joined_array)) #remove one

#clear()
joined_array.clear()
print('Remove everything using clear(): ' + str(joined_array)) #remove all


#sort() --- ascending order
random_numbers.sort()
print('Sorted numbers: ' + str(random_numbers))

fruit_list.sort()
print('Sorted Fruits: ' + str(fruit_list)); #small m is sorted differently on the basis of ascii

#reverse()---> descending order

random_numbers.reverse()
print('Reversed numbers: ' + str(random_numbers))

fruit_list.reverse()
print('reversed Fruits: ' + str(fruit_list)); #small m is reversed differently on the basis of ascii

#copy()

print('Before copying flowers: ' + str(copied_list))  #new copied list
copied_list = flowers.copy()
print('After copying flowers: ' + str(copied_list))  #new copied list


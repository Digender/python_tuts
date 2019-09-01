#tuples are immutable lists, that cnot be modified
#they are similar to arrays

tuples = (4, 5, 6, 2, 5)
print(tuples[2])

#count()
print('Values in Tuple ' + str(tuples.count(5))) # basically counts the number of times its present same for list

#index
print('Index in Tuple ' + str(tuples.index(6, 0, 10))) # index of first element found here 6 from range 0 to 10

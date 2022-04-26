list_a = [1, 2, 3, 4, 5]
list_A = list(range(1, 6))  # Same as list_a
list_b = ['a', 'b', 'c', 'd', 'e']
list_c = ['donga', 'puku', 'munda', 'fuck', 'dick']

combinedItems = zip(list_A, list_b, list_c)
combinedItemsList = list(combinedItems)

print(combinedItems)
print(combinedItemsList)

for x, y, z in combinedItemsList:
    print(x)
    print(y)
    print(z)

# check to see if an object is present in a list
print('\n------------------')
print('z' in list_b)  # Result is bool = False
'''This works with
1. Dictionaries
2. Lists
3. Tuples
'''

# Handy Arithmatic function
# min, max
print('\n---------------')
list_x = [1,2,3,4,5]
print(max(list_x))
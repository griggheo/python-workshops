print('Initializing a list')
myList = [1, 2, 3, 4, 3, 5, 2, 6, 1, 7, 1, 6, 9]
print(f'myList = {myList}')

print('Appending an element to a list')
myList.append(10)
print(f'myList = {myList}')

print('Deleting an element from a list removes only the first element it finds')
myList.remove(6)
print(f'myList = {myList}')

print('Getting the length of a list')
print(f'len(myList) = {len(myList)}')

print('Getting the minimum and maximum from the elements of a list')
print(f'min(myList) = {min(myList)}')
print(f'max(myList) = {max(myList)}')

print('Getting the count of the occurrences of an element in a list')
#for element in [1, 5, 9, 20]:
for element in [1, 3, 5, 9]:
    print(f'myList.count({element}) = {myList.count(element)}')

print('Getting the index of the first occurrence of an element in a list')
for element in [1, 3, 5, 9]:
    print(f'myList.index({element}) = {myList.index(element)}')

print('Sorting a list in ascending order')
myList.sort()
print(f'myList sorted in ascending order: {myList}')

print('Sorting a list in descending order')
myList.sort(reverse=True)
print(f'myList sorted in descending order: {myList}')

print('Creating an empty dict using empty brackets')
myDict = {}
print(f'myDict = {myDict}')
 
print('Creating an empty dict using dict()')
myDict = dict() 
print(f'myDict = {myDict}')

print('Creating a dictionary with literals')
myDict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
}
print(f'myDict = {myDict}')

print('Creating a dictionary by passing parametrs in dict constructor')
myDict = dict(one = 1,
              two = 2,
              three = 3,
)
print(f'myDict = {myDict}')

print('Creating a dictionary from a list of tuples')
tuples = [("one" , 1), ("two" , 2), ("three" , 3)]
myDict = dict(tuples)
print(f'myDict = {myDict}')

print('Creating a Dictionary by a list of keys and initializing all with the same value')
string_keys = ["one", "two", "three"]
myDict = dict.fromkeys(string_keys, 100)
print(f'myDict = {myDict}')

# construct a list with a for loop
cubes = []
for i in range(10):
    cubes.append(i*i*i)
print("Cubes with for loop:", cubes)

# construct a list with map

fahrenheit = [52, 74, 0, 31, -9, 20, 41, 81]
def fahrenheit2celsius(t):
    return (t - 32) / 1.8

celsius = map(fahrenheit2celsius, fahrenheit)
print("Celsius with map:", list(celsius))

# construct lists with list comprehensions

cubes2 = [i*i*i for i in range(10)]
print("Cubes with list comprehension:", cubes2)

celsius2 = [fahrenheit2celsius(i) for i in fahrenheit]
print("Celsius with list comprehension:", list(celsius2))

# using conditions in list comprehensions

mild_temps = [i if i > 70 else 0 for i in fahrenheit]
print("Mild temperatures:", mild_temps)

def get_mild_temp(temp):
    return temp if temp > 70 else 0

mild_temps2 = [get_mild_temp(i) for i in fahrenheit]
print("Mild temperatures with get_mild_temp:", mild_temps2)

# get positive temperatures
positive_temps_fahrenheit = [i for i in fahrenheit if i > 0]
print("Positive temps in Fahrenheit:", positive_temps_fahrenheit)

positive_temps_celsius1 = [i for i in map(fahrenheit2celsius, fahrenheit) if i > 0]
print("Positive temps in Celsius with fahrenheit2celsius:", positive_temps_celsius1)

positive_temps_celsius2 = [i for i in map((lambda t: (t-32)/1.8), fahrenheit) if i > 0]
print("Positive temps in Celsius with lambda:", positive_temps_celsius2)


"""
https://www.pydanny.com/python-partials-are-fun.html
"""

from functools import partial

def modulo(number, factor):
    return number % factor

def modulo3(number):
    return modulo(number, 3)

def modulo7(number):
    return modulo(number, 7)

n = 83274823
print(f"Modulo 3 of {n} is {modulo3(n)}")
print(f"Modulo 7 of {n} is {modulo7(n)}")

mod3 = partial(modulo, factor=3)
mod7 = partial(modulo, factor=7)

print(f"Modulo 3 of {n} with partial is {mod3(n)}")
print(f"Modulo 7 of {n} with partial is {mod7(n)}")

modulo_partials = []
range_min = 2
range_max = 20
for x in range(range_min, range_max):
    f = partial(modulo, factor=x)
    modulo_partials.append(f)
print("modulo_partials list:", modulo_partials)

# Using a list comprehension
modulo_partials_via_list_comprehension = [partial(modulo, factor=x) for x in range(range_min, range_max)]
print("modulo_partials_via_list_comprehension list:", modulo_partials_via_list_comprehension)

# test if a number is divisible by any of the numbers range_min through range_max-1
n = 207330297102173
factor = 2
for f in modulo_partials:
    print(f"Modulo {factor} of {n} is {f(n)}") 
    if f(n) == 0:
        print(f"Number {n} is divisible by {factor}!")
    factor += 1       

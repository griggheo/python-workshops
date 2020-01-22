"""
alvinalexander.com: FP = Pure Functions + Immutable Values
"""

"""
Pure functions

* The output of a pure function depends only on 
(a) its input parameters and
(b) its internal algorithm.
  - This is unlike an OOP method, which can depend on other fields in the
    same class as the method.

* A pure function has no side effects, meaning that it does not read anything
from the outside world or write anything to the outside world.
  - It does not read from a file, web service, UI, or database, and does not
    write anything either.

* As a result of those first two statements, if a pure function is called with an
input parameter x an infinite number of times, it will always return the same
result y
  - Referential Transparency: an expression is referentially transparent if it can 
    be replaced by its resulting value without changing the behavior of the
    program. 
"""

# examples of pure functions

import math

a = math.ceil(2.58)
print("Ceil", a)

b = math.log(100)
print("Log:", b)

c = len("this is a string")
print("Len:", c)

d = max([2,1,0,8])
print("Max:", d)

def add2(x):
    return (x+2)

print("Add 2:", add2(3))

# examples of impure functions

from datetime import datetime
import time

x1 = datetime.now()
print("Timestamp:", x1)

time.sleep(0.1)

x2 = datetime.now()
print("Timestamp:", x2)

import random

y1 = random.choice(range(100))
print("Random choice:", y1)

y2 = random.choice(range(100))
print("Random choice:", y2)

z1 = input('Please enter a number--> ')
print("Input:", z1)

z2 = input('Please enter a number--> ')
print("Input:", z2)


### pure functions vs. side effects

my_list = [1,2,3,4,5]
my_other_list = [11,12,13,14,15]

def pure_multiplication(numbers, factor):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * factor)
    return new_numbers

list_from_pure_multiplication = pure_multiplication(my_list, 3)
print("my_list=", my_list)
print("list_from_pure_multiplication=", list_from_pure_multiplication)

def side_effects_multiplication(numbers, factor):
    for i, n in enumerate(numbers):
        numbers[i] = n * factor
my_list_for_side_effects_multiplication = [1,2,3,4,5]
print("my_list_for_side_effects_multiplication BEFORE=", my_list_for_side_effects_multiplication)

side_effects_multiplication(my_list_for_side_effects_multiplication, 3)
print("my_list=", my_list)
print("my_list_for_side_effects_multiplication AFTER=", my_list_for_side_effects_multiplication)

### immutability: lists vs tuples
my_mutable_list = ["a", "b", "c"]
my_immutable_tuple = ("a", "b", "c")
my_mutable_list[1] = "be"
print("Mutated list:", my_mutable_list)
# this will fail:
# my_immutable_tuple[2] = "b2"

"""
https://kite.com/blog/python/functional-programming/
"""

my_words = ['fox', 'boss', 'orange', 'fairy', 'cup']

# function with side effects

def pluralize1(words):
    for i, word in enumerate(words):
        if word.endswith('s') or word.endswith('x'):
            plural = word + 'es'
        elif word.endswith('y'):
            plural = word[:-1] + 'ies'
        else:
            plural = word + 's'
        #print(f"Plural of {word} is {plural}")
        words[i] = plural

def test_pluralize1():
    pluralize1(my_words)
    print(my_words)
    assert my_words == ['foxes', 'bosses', 'oranges', 'fairies', 'cups']

test_pluralize1()
# second call with fail
#test_pluralize1()

my_words = ['fox', 'boss', 'orange', 'fairy', 'cup']

# function with no side effects

def pluralize2(words):
    result = []
    for word in words:
        if word.endswith('s') or word.endswith('x'):
            plural = word + 'es'
        elif word.endswith('y'):
            plural = word[:-1] + 'ies'
        else:
            plural = word + 's'
        #print(f"Plural of {word} is {plural}")
        result.append(plural)
    return result

def test_pluralize2():
    # note function signature
    result = pluralize2(my_words)
    print(result)
    assert result == ['foxes', 'bosses', 'oranges', 'fairies', 'cups']

test_pluralize2()
test_pluralize2()
test_pluralize2()

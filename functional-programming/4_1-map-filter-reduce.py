my_list = [1,2,3,4,5]

### iteration vs. map
list_from_iteration = []
for i in my_list:
  j = 2 * i
  list_from_iteration.append(j)
print("List from iteration:", list_from_iteration)

list_from_map = list(map(lambda x: 2 * x, my_list))
print("List from map:", list_from_map)

### iteration vs. filter
even_numbers_from_iteration = []
odd_numbers_from_iteration = []
for i in my_list:
  if (i % 2 == 0):
    even_numbers_from_iteration.append(i)
  else:
    odd_numbers_from_iteration.append(i)
print("Even numbers from iteration:", even_numbers_from_iteration)
print("Odd numbers from iteration:", odd_numbers_from_iteration)

even_numbers_from_filter = list(filter(lambda x: True if (x % 2 == 0) else False, my_list))
print("Even numbers from filter:", even_numbers_from_filter)

odd_numbers_from_filter = list(filter(lambda x: True if (x % 2 == 1) else False, my_list))
print("Odd numbers from filter:", odd_numbers_from_filter)

### iteration vs. reduce
sum_from_iteration = 0
for i in my_list:
  sum_from_iteration += i
print("Sum from iteration:", sum_from_iteration)

from functools import reduce

sum_from_reduce = reduce((lambda x, y: x + y), my_list)
print("Sum from reduce:", sum_from_reduce)

# combine map, filter and reduce

# find the sum of odd numbers

sum_of_odds = reduce((lambda x, y: x + y), filter(lambda x: True if (x % 2 == 1) else False, my_list))
print("Sum of odd numbers:", sum_of_odds)

# find the sum of even numbers

def is_even(x):
  return False if x % 2 else True

sum_of_evens = reduce((lambda x, y: x + y), list(filter(is_even, my_list)))
print("Sum of even numbers:", sum_of_evens)

# find the sum of squares of odd numbers

sum_of_squares_of_odds = reduce((lambda x, y: x + y), 
                          map((lambda y: y*y), 
                          filter(lambda x: True if (x % 2 == 1) else False, my_list)))
print("Sum of squares of odd numbers:", sum_of_squares_of_odds)

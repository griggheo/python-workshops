my_list = [1,2,3,4,5]
my_other_list = [11,12,13,14,15]

#### functions as objects
def my_sum(a, b):
  return a + b
sum_my_lists = my_sum
print("Sum my lists:", sum_my_lists(my_list, my_other_list))

# normal iteration
def iterate(list_of_items):
    for item in list_of_items:
        print("Item in iterate function:", item)
iterate(my_list)

# apply custom function to each element in list 
def iterate_custom(list_of_items, custom_func):
   for item in list_of_items:
        custom_func(item)

def my_func(item):
  result = item * item
  print("Result in my_func:", result)
  return result

iterate_custom(my_list, my_func)

# regular function vs. lambda
def raise_to_power(x, y):
  return x ** y
result = raise_to_power(2, 10)
print("Raise to power from regular function:", result)

raise_to_power_lambda = lambda x, y: x ** y
print("Raise to power from lambda:", raise_to_power_lambda(2, 10))
print("Another lambda:", 
    (lambda x, y, z: (x + y) * z)(2,3,4))

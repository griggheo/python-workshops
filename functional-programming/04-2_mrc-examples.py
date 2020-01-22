"""
https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

Functional code is characterised by one thing: the absence of side effects. 
It doesn’t rely on data outside the current function, and it doesn’t change data 
that exists outside the current function. 

Every other “functional” thing can be derived from this property. 

Use it as a guide rope as you learn.
"""

### count how often the word 'Sam' appears in a list of strings

sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

# using a loop

sam_count1 = 0
for sentence in sentences:
    sam_count1 += sentence.count('Sam')

print(f"Sam appears {sam_count1} times")

# using reduce

from functools import reduce
sam_count2 = reduce(lambda a, x: a + x.count('Sam'),
                   sentences,
                   0)
print(f"Sam appears {sam_count2} times")


### compute average height

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

# using a loop

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height1 = height_total / height_count
    print(f"Average height is {average_height1}")

# using map, filter and reduce

heights = list(map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people)))

if len(heights) > 0:
    from operator import add
    average_height2 = reduce(add, heights) / len(heights)
    print(f"Average height is {average_height2}")


# write declaratively, not imperatively

from random import random

print("Car positions - imperative style")

time = 5
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1
    print('')
    for i in range(len(car_positions)):
        # move car
        if random() > 0.3:
            car_positions[i] += 1

        # draw car
        print('-' * car_positions[i])


print("Car positions - declarative style")

def move_cars(car_positions):
    return list(map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions))

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print('')
    print('\n'.join(list(map(output_car, state['car_positions']))))

def race(state):
    print(f'in race: state = {state}')
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 4,
      'car_positions': [1, 1, 1]})

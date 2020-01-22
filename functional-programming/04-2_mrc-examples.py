"""
https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming
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

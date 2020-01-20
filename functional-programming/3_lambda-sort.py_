# Peter Pan: wget https://www.gutenberg.org/files/16/16-0.txt
# Walden: wget http://www.gutenberg.org/files/205/205-0.txt
# Tom Sawyer: wget https://www.gutenberg.org/files/74/74-0.txt

import os
import re
import sys

def is_letter(c):
    #if c in [" ", "'", '"', ',', '.']:
    #    return False
    #if re.match('[a-zA-Z0-9]+', c):
    #    return True
    #return False
    #return re.match('[a-zA-Z0-9]+', c)
    return re.match('[a-zA-Z]+', c)

def sort_characters(characters, print_chars):
    # sort keys by values
    sorted_characters = sorted(characters, key=lambda k: characters[k], reverse=True)
    print("Sorted keys:", sorted_characters)
    if print_chars:
        for item in sorted_characters:
            print(f'Character {item} appears {characters[item]} times')
    return sorted_characters

# main program

print(sys.argv)
if len(sys.argv) == 1:
    print('Please specify a file name as an argument.')
    sys.exit(1)

filenames = sys.argv[1:]
print("here are the arguments to the program")
print(filenames)
characters = {}

for filename in filenames:

#filename = sys.argv[1]

#counter = 2000
#i = 0
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            #print(line)
            chars = str(line)
            for c in chars:
                if not is_letter(c):
                    continue
                c = c.lower()
                characters[c] = characters.get(c, 0) + 1
    #        i += 1
    #        if i >= counter:
    #            break

print(characters)

sorted_characters = sort_characters(characters, print_chars=False)

print("Top Ten")
top = ",".join(sorted_characters[:10])
print(top)

print("Bottom Five")
bottom = " ".join(sorted_characters[-5:])
print(bottom)

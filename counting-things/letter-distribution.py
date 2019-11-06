import os
import re
import sys

def is_letter_or_digit(c):
    #if c in [" ", "'", '"', ',', '.']:
    #    return False
    #if re.match('[a-zA-Z0-9]+', c):
    #    return True
    #return False
    return re.match('[a-zA-Z0-9]+', c)

if len(sys.argv) == 1:
    print('Please specify a file name as an argument.')
    sys.exit(1)

filename = sys.argv[1]

counter = 2000
i = 0
characters = {}
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        #print(line)
        chars = str(line)
        for c in chars:
            if not is_letter_or_digit(c):
                continue
            c = c.lower()
            characters[c] = characters.get(c, 0) + 1
        i += 1
        if i >= counter:
            break

print(characters)
print(sorted(characters, key=lambda k: characters[k], reverse=True))
for item in sorted(characters, key=lambda k: characters[k], reverse=True):
    print(f'Character {item} appears {characters[item]} times')


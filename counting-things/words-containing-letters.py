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

def sort_words(word_count, verbose=False):
    # sort keys by values
    sorted_words = sorted(word_count, key=lambda k: word_count[k], reverse=True)
    if verbose:
        print(sorted_words)
        for item in sorted_words:
            print(f'word {item} appears {word_count[item]} times')
    return sorted_words

# main program

if len(sys.argv) < 3:
    print('Please specify a file name and a list of letters separated by space')
    print('Example: pyhton words-containing-letters.py barrie-peter-pan.txt a w b')
    sys.exit(1)

filename = sys.argv[1]
print(f'Got filename: {filename}')
letters = sys.argv[2:]
print(f'Got letters: {letters}')

counter = 20
i = 0
word_count = {}
with open(filename) as f:
    for line in f:
        line = line.rstrip()
#        print(type(line))
#        print(line)
        words = line.split()
#        print(words)
        for word in words:
            for letter in letters:
                if word.find(letter) != -1:
                    print(f'Found word {word} containing the letter {letter}')
                    word_count[word] = word_count.get(word, 0) + 1
        i += 1
        if i >= counter:
            break

print(word_count)

sorted_words = sort_words(word_count, verbose=True)

print("Top Ten")
top = " ".join(sorted_words[:10])
print(top)

print("Bottom Five")
bottom = " ".join(sorted_words[-5:])
print(bottom)

print("Looping through sorted word list using for loop:")
for word in sorted_words:
    print(word)

print("Looping through sorted word list using while loop with counter:")
i = 0
while i < len(sorted_words):
    print(sorted_words[i])
    i += 1

print("Looping through sorted word list using enumerate:")
for i, word in enumerate(sorted_words):
    print(i, word)

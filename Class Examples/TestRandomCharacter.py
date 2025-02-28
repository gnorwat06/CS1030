#Description: Testing the functions in the RandomCharacter module

#Import the random character module
from RandomCharacter import *

#Number of characters to be generated
NUM_OF_CHARS = 175

#Number of characters to be displayed per line
CHARS_PER_LINE = 25

#Print random characters between 'a' and 'z'
for i in range(NUM_OF_CHARS):
    #Display the lowercase letter
    print(getRandomLowerCaseLetter(), end = '')

    #Check if we have 23 on line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()

#Print random characters between 'A' and 'Z'
for i in range(NUM_OF_CHARS):
    #Display the lowercase letter
    print(getRandomUpperCaseLetter(), end = '')

    #Check if we have 23 on line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()

#Print random characters between '0' and '9'
for i in range(NUM_OF_CHARS):
    #Display the lowercase letter
    print(getRandomDigitCharacter(), end = '')

    #Check if we have 23 on line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

print()

#Print random characters between ASCII Table value
for i in range(NUM_OF_CHARS):
    #Display the lowercase letter
    print(getRandomASCIICharacter(), end = '')

    #Check if we have 23 on line
    if (i + 1) % CHARS_PER_LINE == 0:
        print() #Jump to next line

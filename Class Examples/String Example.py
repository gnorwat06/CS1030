#Descrition: Looking into strings and the str class

#import the turlte module
from turtle import *

#A string is a sequence of characters

#Strings must be enclosed in a matching single or double quotes
letter = 'A' #Letter = "A" its the same
numChar = '4' #numChar = "4" its the same
message = "Good morning" # 'Good morning'

#Empty string can be single or double quotes
x = ' '
y = " "

#Note: Special kind of string denoted by triple single quotes
#This preserves the tab and carriage returns
print('''   There are three ways to represent strings:
    1. Single-Quotes
    2. Double-Quotes
    3. Triple-Quotes.''')


#Unicode is an encoding scheme for representing international characters
#write("\u6B22 \u8FCE \u03B1 \u03B2 \u03B3",font=("Times",30))

uniLetter = "\u0041"
print(uniLetter)

#The ord and char function
#ord(ch) return the ASCII code value for the character
#chr(code) return the ASCII character for the code
print(ord('A'))
print(chr(65))
print(chr(ord('a') - ord('A') + 20))

#Escape sequences for special characters
#Print a message with quotation marks in the output
#print("He said, "John's program is easy to read"")

#One way to fix is by using tripple quotes
print('''He said, "John's program is easy to read"''')

#Other way is to use escape sequences
#most common: \n = newline, \t tab (8 spaces), \\, \', \"
print("\tHe said,\n \"John's program is easy to read\"")

#Printing without the NewLine
print("AAA", end = '')
print("BBB", end = '123')
print("CC", end = '$$')
print("DD", end = ' ')
print("EE", end = '!')
print()
#the str function can be used to return a string from any data type
s = str(3.5) #Return a string object
print(type(s),s)

#The concatenation + and Repetition * operator
#join / concatenate two strings using +
s1 = "Welcome"
s2 = "Python"
s3 = s1 + " to " + s2
print(s3)

#we can use the augmented assignemtn opperator +=
s3 += "! Hello, World\n"
print(s3)

#* operator to concatenate the same string multiple times
print(s3 * 5)

#Reading strings from the console
#to read a string from the console use the input function
'''
firstName = input("Enter your first name: ")
mi = input("Enter your middle initial: ")
lastName = input("Enter your last name: ")

print("Employee Name:",firstName,mi,lastName)
'''

#The in and not in operators
#Testing whether a string is in another sting
s1 = "Welcome"
print("me" in s1)
print("Wel"  not in s1)
'''
s = input("Enter a string: ")

if "Python" in s:
    print("Python is in",s)
else:
    print(s,"is not in the string")
'''

#Comparint Strings
#Python compares strings by comparing their corresponding characters
#we do this by comparing their ASCII code
print("green" == "glow")
print("green" != "glow")
print("green" > "glow")

#Built-in functions fro strings
#len(), max(), min()
#len function returns the number of characters in a string
print(len(s1))

#max and min functions return the largest or smalleset character
print(max(s1))
print(min(s1))

if len(s1) % 2 == 0:
    print(s1,"Contains an even number of characters")
else:
    print(s1,"Contains an odd number of characters")

#Index operator []
#A character in the string can be accessed through the index operator:
#INdexes are 0 based
#range from 0 to len(string) - 1
s = "Hello"
s1 = s[2]
print(s1)

#we can use negative numbers as indexes as wel to reference positinos
#relative to the end of the string
s2 = s[-2]
print(s2)

#WARNING: Strings are immutable objects. Their contents cannot be changed
#s[2] = 'a'

#Slicing operator [starting index : ending index - 1]
#return a slice of a string
#the slice is a substring  from the existing string
print(s[2:])
print(s[:-2])

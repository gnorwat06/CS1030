'''
Description: converting a hexadecimal digit to a decimal

Base 16: 0-9 and A-F
A = 10 (65 ASCII Code)
B = 11 (66 ASCII Code)
C = 12 (67 ASCII Code)
D = 13 (68 ASCII Code)
E = 14 (69 ASCII Code)
F = 15 (70 ASCII Code)
'''
#import the sys module
import sys

#Prompt the user to input a hexadecimal character
#We will use the .upper() method to just handle uppercase letters
hexDigit = input("Enter a hex digit: ").upper()

#Check if the hex digit has exactly one character
if len(hexDigit) != 1:
    print("You must enter exactly one character")
    sys.exit()

#display decimal value for the hex digit
if hexDigit <= 'F' and hexDigit >= 'A':
    #hexdigit = A
    #Value = A - A + 10
    #Value = 65 - 65 + 10
    value = ord(hexDigit) - ord('A') + 10
    print(f"The decimal value for hex digit {hexDigit} is {value}")

elif hexDigit.isdigit():
    print(f"The decimal value of hex digit {hexDigit} is {hexDigit}")

else:
    print(f"{hexDigit} is an invalid input")

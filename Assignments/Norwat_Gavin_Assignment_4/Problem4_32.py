#Gavin Norwat
#700746314
#Assignment 4 / Problem4.32
#Description: Convert decimal to hex
'''
Base 16: A-F
A = 10 
B = 11 
C = 12 
D = 13 
E = 14
F = 15 
'''

#import sys
import sys
#prompt user for decimal value
decimal = int(input("Enter a decimal integer value (0 to 15): "))

#Check to see if value is between 0 and 15
if decimal < 0 or decimal > 15:
    print("The value must be between 0 and 15")
    sys.exit()

#convert value to hex
if decimal >= 0 and decimal <= 9:
    print(f"The hex value is {decimal}")
    sys.exit()

if decimal >=10 and decimal <= 15:
    print("The hex value is",(chr(decimal + 55)))





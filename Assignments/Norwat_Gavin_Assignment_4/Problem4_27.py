#Gavin Norwat
#700746314
#Assignment 4 / Problem4.27
#Description: map letters to numberes on a telephone

#import sys
import sys

#Prompt the user to input a character
ch = input("Enter an uppercase letter: ").upper()

#create a multi-way or match-case
#You can use the pipe operator(|) for the or in a match statement
match ch:
    case 'A' | 'B' | 'C': number = 2
    case 'D' | 'E' | 'F': number = 3
    case 'G' | 'H' | 'I': number = 4
    case 'J' | 'K' | 'L': number = 5
    case 'M' | 'N' | 'O': number = 6
    case 'P' | 'Q' | 'R' | 'S': number = 7
    case 'T' | 'U' | 'V': number = 8
    case 'W' | 'X' | 'Y' | 'Z': number = 9
    case _:
        print("Invalid Input")
        sys.exit()

#Print the results
print(f"The corresponding number is {number}")
    

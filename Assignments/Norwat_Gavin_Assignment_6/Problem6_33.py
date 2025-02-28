#Gavin Norwat
#700746314
#Assignment 6 / Problem 6_33
#Description: Find the area of a pentagon using funcitons

#import math module

import math

#Defind the area functin

def area(s):
    a = (5 * s**2)/( 4 * math.tan((math.pi/5)))

    print(f"The area of the pentagon is {a}")

#define the main functin

def main():
    s = float(input("Enter the side: "))

    #invoke the area function
    area(s)

#invoke the main funciton
main()

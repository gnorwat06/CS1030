#Gavin Norwat
#700746314
#Assignment 6 / Problem 6_34
#Description: Find the area of a polygon using funcitons

#import the math function
import math

#create the area funciton
def area(n, side):

    #compute the area
    
    a = ((n * side ** 2)/(4 * math.tan(math.pi / n)))
    
    #Display results
    print(f"The area of the polygon is {a}")

#Create the main function
def main():
    #ask the user the number of side and the lenght of the sides

    n = int(input("Enter the number of sides: "))

    side = float(input("Enter the side: "))

    #invoke the area function
    area(n, side)

#invoke the main function
main()
    

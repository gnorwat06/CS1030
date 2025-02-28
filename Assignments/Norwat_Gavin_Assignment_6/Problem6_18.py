#Gavin Norwat
#700746314
#Assignment 6 / Problem 6.18
#Description: Write a function that displays a n-by-n matrix

#Import random
from random import randint

#Create a main function
def main():
    #Prompt the user to input the vale for the size of the matrix
    n = int(input("Enter n: "))

    #Invoke the printMatrix Function
    printMatrix(n)

#Void type funciton to display the matrix
def printMatrix(n):

    #Outer for loop controls the rows of the matrix
    for i in range(1, n + 1):

        #Inner for loop control the column informatin
        for j in range(1, n + 1):
            #Generate a random 0 or 1
            print(randint(0,1), end = ' ')

        #Jump to the next row
        print()

#Invoke the main function
main()

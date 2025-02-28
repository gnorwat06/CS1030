#Gavin Norwat
#700746314
#Assignment 6 / Problem 6.5
#Description: Prompt the user to enter three numbers the displa them in ascending
#order

#Create the sort function
def displaySortedNumbers(num1, num2, num3):

    #use conditional statement to find the order of the numbers
    if num1 <= num2 <= num3:
        print(f"The sorted numbers are {num1}, {num2}, {num3}.")
    elif num1 <= num3 <= num2:
        print(f"The sorted numbers are {num1}, {num3}, {num2}.")
    elif num2 <= num1 <= num3:
        print(f"The sorted numbers are {num2}, {num1}, {num3}.")
    elif num2 <= num3 <= num1:
        print(f"The sorted numbers are {num2}, {num3}, {num1}.")
    elif num3 <= num1 <= num2:
        print(f"The sorted numbers are {num3}, {num1}, {num2}.")
    else:
        print(f"The sorted numbers are {num3}, {num2}, {num1}.")

#Create the main function
def main():

    num1 = float(input("Enter number1: "))
    num2 = float(input("Enter number2: "))
    num3 = float(input("Enter number3: "))

    #invoke the sort function
    displaySortedNumbers(num1, num2, num3)

#invoke the main function
main()

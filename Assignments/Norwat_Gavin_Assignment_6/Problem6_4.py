#Gavin Norwat
#700746314
#Assignment 6 / Problem 6.4
#Description: display an integer in reverse order

#Create the reverse function
def reverse(num):

    
    # Convert the integer to a string, reverse it, and convert it back to an integer
    reversed_num = int(str(num)[::-1])
    
    # Display the reversed integer
    print(reversed_num)

#Define the main function
def main():

      # Prompt user to enter an integer
    num = int(input("Enter an integer: "))

    #Invoke the reverse function
    reverse(num)

#Invoke the main function
main()

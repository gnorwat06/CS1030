#Description: Example of passing arguments by reference values

#Create the main function
def main():

    #Initialize x to 1
    x = 1

    #Display the value of x before invoking the increment function
    print(f"Before the call/invoke, x is {x}")

    #invoke the increment function
    increment(x)

    #Display the results after the function call
    print(f"After the call/invoke, x is {x}")

#Create the increment function
def increment(n):

    #Increment n by 1
    n += 1

    #display the value of n
    print(f"\t\n inside the function n is {n}")

#invoke the main function
main()

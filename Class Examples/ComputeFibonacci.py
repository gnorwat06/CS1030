'''
Computing Fibonacci Numbers

The Fibonacci series begins with 0 and 1 (Base Case / Stopping Case)
and each subsequent number is the sum of the preceding two indices

Examples:
index 0 = 0
index 1 = 1
index 2 = 1
index 3 = 2
index 4 = 3

Note: Python evaluates left to right
'''
#Create the main funciton
def main():
    #Prompt the user to enter a value for our index
    index = int(input("Enter an index for a Fibonacci number: "))

    #Invoke and display our fibonacci number
    print(f"The Fibonacci number at index {index} is {fib(index)}")

#The function for finding the number/value with its index
def fib(index):

    #We will have 2 base cases if we hit index 0 or 1
    if index == 0: #Base case
        return 0
    elif index == 1: #Base case
        return 1

    #Calling the funciton with a index greater than or equal to 2
    #So we can divide the problem into two subproblems
    else:
        return fib(index - 1) + fib(index - 2)

#invoke the main
main()

'''
Tail Recursion Example

Note: A recursive function is said to be tail recursive if there are no pending
operations to be preformed on return
'''
#return the factorial for a specified number
def factorial(n):
    return factorialHelper(n,1) #calling auxiliary funciton

#Auxiliary tail-recursive funciton for factorial
def factorialHelper(n,result):

    #Base Case
    if n == 0:
        return result
    else:
        #Recursive call
        return factorialHelper(n - 1, n * result)

#Create the main funciton
def main():
    #Prompt the user to input a positive integer
    n = int(input("Enter a nonnegative integer: "))

    #Display the results / invoke the factorial function

    print(f"Factorial of {n} is {factorial(n)}")

#Invoke the main
main()

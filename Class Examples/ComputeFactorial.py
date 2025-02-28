'''
A recursive function is one that invokes itself (direct recursion)

recursive call can result in many more recursive calls, because the functions keep
on dividing a sub problem into a new subproblem

'''
#Create the main function
def main():
    #Prompt the user to enter a positive integer
    n = int(input("Enter a non negative integer: "))

    #display results and invoke factorial function
    print(f"Factorial of {n} is {factorial(n)}")

#return the factorial for a specified numbber
def factorial(n):
    #base case / stoppin condiiton (Factorial(0) = 1)
    if n == 0:
        return 1
    else:
        #recursive call, since we are calling ourselves
        #Notice: we are decrementing n each call till we hit
        #the base case
        return n * factorial(n - 1)

#invoke main
main()

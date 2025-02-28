#Description: Creating a module to compute the greatest common divisor

#Create a function to take two integer and find the GCD
def gcd(n1,n2):

    #Initialize gdc and k
    gcd = 1
    k = 2 #Possible gcd

    #create a while loop and l.c.c is k cannot exceed the two values
    while k <= n1 and k <= n2:

        #Check if k equally divides into both integers
        if n1 % k == 0 and n2 % k == 0:
            #Update the gcd to k
            gcd = k

        #Increment k by 1
        k += 1

    #Return the gcd back to the caller
    return gcd

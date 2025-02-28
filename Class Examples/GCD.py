#Description: Find the greatest common divisor
#1 is a common divisor but may not be the gcd so we will check k against n1 and n2

#prompt the user to input two integers
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

#Set gcd to 1
gcd = 1

#k will start at 2
k = 2

#create a while loop to check if k is smaller or requal to our two numbers
while k <= n1 and k <= n2:
    #k equally divides into n1 and n2 set new gcd to the value of k
    if n1 % k == 0 and n2 % k == 0:
        gcd = k

    #increment k by 1
    k += 1

#Display the results
print(f"The greatest common divisor for {n1} and {n2} is {gcd}")

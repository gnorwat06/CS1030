#Description: Testing the GCD MOdule

#Import GCD
from GCDfunction import gcd

#Prompt the user to input two integerse
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

#Display the results / invoke the GCD function
print(f"The greatest common divisor for {n1} and {n2} is {gcd(n1,n2)}")

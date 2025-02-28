#Description: Displaying the first 50 prime numbers and we only want 10 per line

#number or pfomres to display
NUM_OF_PRIMES = 10000

#display 10 per line
NUM_OF_PRIMES_PER_LINE = 10

#Count the number of prime
count = 0

#a number to be tester for primeness
number = 2

#Display the heading
print("The first 50 prime numbers are: ")

#Repeatedly find prime until we reach 50
while count < NUM_OF_PRIMES:

    #Assume the number is prime
    isPrime = True #is the current number prime

    #Test if the number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            #If true, the number is not prime
            isPrime = False
            break ##xit the loo

        #increment the divisor
        divisor += 1


    #Display the prime number and increase the count
    if isPrime:
        #Increment the count
        count += 1

        #Display the primes
        print(f"{number:5d}", end = '')

        if count % NUM_OF_PRIMES_PER_LINE == 0:
            #Display the number and advance to the new line
            print()

    #Check if the next number is prime
    number += 1

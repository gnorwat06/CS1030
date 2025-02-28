#Gavin Norwat
#700746314
#Assignment 5 / Problem 5.1
#Description: count positive and negative numbers and compute the average
#Note: display average as floating point number
#Note: 0 is our sentinel value (exit on 0)

#Create an initialized variable
countPositive = 0
countNegative = 0
count = 0 #numbers we input
total = 0

#Prompt the user to enter a integer
num = int(input("Enter an integer, the input ends if it is 0: "))

#Create the while loop L.C.C is if the number is 0
while num != 0:
    #Multi-way check if it is positive or negative
    if num > 0:
        countPositive += 1
    elif num < 0:
        countNegative += 1

    #add number to toal
    total += num

    #Increment the count by 1
    count += 1

    #read the next input from the user
    num = int(input("Enter an integer, the input ends if it is 0: "))

#Display the results
if count == 0:
    print("No numbers are entered except 0")
else:
    print(f"The number of positives is {countPositive}")
    print(f"The number of negatives is {countNegative}")
    print(f"The total is {total}")
    print(f"The average is {total / count}")

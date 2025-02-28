#Description: the continue key word will skip everything (statments) below it
#and go to the next itteration

#Create a total variable
total = 0
number = 0

#Create a while loop to iterate until we hit 20
while number < 20:

    #Increment number by 1
    number += 1

    #We do not want to add the value 10 or 11 to the total
    if number == 10 or number == 11:
        continue #we will skip over everything below this point

    #add the number into the total
    total += number

#Display the total
print(f"The total is {total}")
print(f"The number is {number}")

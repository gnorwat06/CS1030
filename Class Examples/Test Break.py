#Description: The keyword break will break out of the loop

#Create a variable to store the total
total = 0
number = 0

#Create a while loop to exit if or when we hit 20
while number < 20:

    #Add/increment number by 1
    number += 1

    #Add the number to the total
    total += number

    #If our total is greater or equal to 100
    #we want to break out of the loop
    if total >= 100:
        break #Breaks the loop


#display the results
print(f"The number is {number}")
print(f"The total is {total}")

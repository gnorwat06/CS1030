#Description: get 3 values from the user and find the its average
'''
Step 1: Prompt the user to input 3 values
Step 2: Add the three values togeather and divide by 3
step 3: Display the results
'''

#Step 1:
num1 = float(input("Enter the first value: "))
num2 = float(input("Enter the second value: "))
num3 = float(input("Enter the third value: "))

#Step 2:
average = (num1 + num2 + num3) / 3

#Step 3:
print("The average of", num1, num2, num3, "is", average)
             
#Line continuation symbol \ the backslash
total = 1 + 2 + 3 + 4 + 5 + \
        6 + 7 + 8 + 9 + 10

print(total)

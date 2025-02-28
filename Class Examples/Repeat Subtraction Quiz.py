#Description: reworking listing 4.4 to repeat the question until you answer correctly

#import random
import random

#generate two random single-digit integeres
num1 = random.randint(0,9)
num2 = random.randint(0,9)

#Swap the values if num1 is less than num2
if num1 < num2:
    num1,num2 = num2,num1
    #print("Swap successful")

#Prompt the student to answer the question
answer = int(input(f"What is {num1} - {num2}? "))

#Repeatedly ask the user the question until correct
while num1 - num2 != answer:
    #reprompt the stuent
    answer = int(input("Wrong answer. Try again!\n" + \
                       f"What is {num1} - {num2}? "))

#display a positive message for the student
print("Great Job!")

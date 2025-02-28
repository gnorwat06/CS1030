#Gavin Norwat
#700746314
#Assignment 7 / problem 37
#Description: Alert if user has already used an answer

#import random
import random

#generate two random single-digit integeres
num1 = random.randint(0,9)
num2 = random.randint(0,9)

#Swap the values if num1 is less than num2
if num1 < num2:
    num1,num2 = num2,num1
    #print("Swap successful")

#create an empty list
lst = []
#Prompt the student to answer the question
answer = int(input(f"What is {num1} - {num2}? "))

#Add the answer to the list
lst.append(answer)

    
#Repeatedly ask the user the question until correct
while num1 - num2 != answer:
    #reprompt the stuent
    answer = int(input("Wrong answer. Try again!\n" + \
                       f"What is {num1} - {num2}? "))

    lst.append(answer)
    #check if they already used the answer
    if answer in lst:
        print(f"You already entered {answer}.")
    

#display a positive message for the student
print("Great Job!")


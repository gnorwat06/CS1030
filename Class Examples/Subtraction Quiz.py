#Description: Develop a program for a first grader to practice subtraction.
'''
Step1: Generate a random single digit integer
Step2: If number1 is less than number 2 swap values
step3: prompt the student to answer the question
step4: display the results but check the answer against the solution
'''

#import the random module
import random

#step1:
num1 = random.randint(0,9)
num2 = random.randint(0,9)

#step2:
if num1 < num2:
    #use simultaneous assignment (chp 2) to swap values
    num1,num2 = num2,num1
    #print("swap successful")

#step3:
answer = int(input(f"What is {num1} - {num2}? "))

#step4:
if num1 - num2 == answer:
    print("Correct!")
else:
    print("Incorrect!")
    print(f"{num1} - {num2} = {num1 - num2}")

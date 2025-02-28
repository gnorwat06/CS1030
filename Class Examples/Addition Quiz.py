#Description: Help first graders practice their addition
'''
Step1: generate two single digit integers
step2: prompt the student to answer the question
step3: check wether their answer is right or wrong
'''

#Import the random module
import random

#step1:
number1 = random.randint(0,9)
number2 = random.randint(0,9)

#Random.random will return a random value between 0.0 and 1.0 excluding 1.0
#extra = random.random()
#print(extra

#random.randrange(a,b -1)
#extra1 = random.randrange(0,10)
#print(extra1)


#Step2:
answer = int(input(f"What is {number1} + {number2}? "))

#or
#answer = int(input("What is " + str(number1) + " + " + str(number2) + "? "))

print(f"{number1} + {number2} = {answer} is {number1 + number2 == answer}")

#extra assigning a boolean value to a variable
#lightsOn = True
#lightsOff = False
#boolean = bool(24)

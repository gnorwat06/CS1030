#Gavin Norwat
#700746314
#Assignment 3 / Problem 3.14
#Description: Write a program that allows the user to guess 0 or 1 for heads or tails

'''
Step1: Prompt user for heads or tails
Step2: Randomly generate 0 or 1
Step4: Display Results
'''

#Step1:
print("Guess head or tail?")
guess = int(input("Enter 0 for head or 1 for tail: "))

#Step 2
#import random
import random
headOrTail = random.randint(0,1)
#print(headOrTail)

#Step3:
if guess == headOrTail and headOrTail == 0:
    print("Correct! It is a Head!")
elif guess == headOrTail and headOrTail == 1:
    print("Correct! It is a Tail")
elif guess != headOrTail and headOrTail == 0:
    print("Sorry, it is a Head.")
else:
    print("Sorry, it is a Tail.")



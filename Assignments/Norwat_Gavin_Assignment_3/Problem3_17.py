#Gavin Norwat
#700746314
#Assignment 3 / Problem 3.17
#Description: Rock Paper Scissor game
'''
Step1: Ask the user rock paper or scissor
step2: Generate answer for the computer
Step3: Compare and display results
'''

#Step1:
user = int(input("scissor (0), rock (1), paper (2): "))

#Step2:
import random
computer = random.randint(0,2)
#print(computer)

#Step3:
if user == 0 and computer == 0:
    print("Computer is scissor, you are scissor too.It is a draw.")
elif user == 1 and computer == 1:
    print("Computer is rock, you are rock too.It is a draw.")
elif user == 2 and computer == 2:
    print("Computer is paper, you are paper too.It is a draw.")
elif user == 0 and computer == 1:
    print("Computer is rock, you are scissor. You loose.")
elif user == 1 and computer == 2:
    print("Computer is paper, you are rock. You loose.")
elif user == 2 and computer == 0:
    print("Computer is scissor, you are paper. You loose.")
elif user == 1 and computer == 0:
    print("Computer is scissor, you are rock. You win!")
elif user == 2 and computer == 1:
    print("Computer is rock, you are paper. You win!")
else:
    print("Computer is paper, you are scissor. You win!")

#Gavin Norwat
#700746314
#Assignment 5 / Problem 5.36
#Description: rework the rock paper scissor game to play until the user or computer
#wins 2 more times than the other

#Import random mondule
import random

#Generate the computer throw
comp = random.randint(0,2)

#Prompt the user to input their throw
user = int(input("Scissor (0), Rock (1), Paper (2): "))

#Create a list to store our word objects
wordBank = ["Scissors","Rock","Paper"]

#create win trackers
userWin = 0
compWin = 0

while (userWin - compWin != 2) or (compWin - userWin != 2):
    #Win Cases
    if (user == 0 and comp == 2) or (user == 1 and comp == 0) or \
       (user == 2 and comp == 1):
        print(f"User threw {wordBank[user]}. Computer threw \
    {wordBank[comp]}. You win!.")
        userWin += 1
    #Lose Cases
    elif (comp == 0 and user == 2) or (comp ==1 and user == 0) or \
         (comp == 2 and user == 1):
        print(f"User threw {wordBank[user]}. Computer threw \
    {wordBank[comp]}. You lose!.")
        compWin += 1
    #Tie Cases
    else:
        print(f"User threw {wordBank[user]}. Computer threw \
    {wordBank[comp]}. You tie!.")

if userWin - compWin == 2:
    print(f"You won {userWin} - {compWin}. Good job!")
else:
    print(f"You lost {compWin} - {userWin}. Better luck next time!")
'''
#Multiway to check the user vs computer
if comp == 0:
    if user == 0:
        print("The computer threw scissor. User threw scissor. It was a tie.")
    elif user == 1:
        print("The computer threw scissor. User threw rock. You win!.")
    elif user == 2:
        print("The computer threw scissor. User threw papaer. You lose!")

elif comp == 1:

elif comp == 2:
'''

#Description: Develop a program to play a 2 digit lottery
'''
Rlue 1: IF the user input matches the lottery in the exact order, award 10,000
dollars.

Rule 2: IF All the digits in the users input matches all the digits in the lottery
number, award them 3,000 dollars

Rule 3: IF one digit in the users input matches a digit in the lotter number,
award 1,000 dollars
'''

#Import random module
import random

#Generate the lottery number
lottery = random.randint(10,99)
#print(lottery)

#Prompt the user to input thier numbers
guess = int(input("Enter your lottery pick(2 digits): "))

#Get the digits from the lottery
lDigit1 = lottery // 10 #Obtains the first digit
lDigit2 = lottery % 10 #Obtains the last digit

#Get the digits from guess
gDigit1 = guess // 10
gDigit2 = guess % 10

#Display the winning lottery nubers
print(f"The Winning Lottery Numbers are {lDigit1}{lDigit2}")

#Create a multi way to check the guess with the rules
if guess == lottery:
    print("Exact Match: You win $10,000!")
elif gDigit2 == lDigit1 and gDigit1 == lDigit2:
    print("Matched all the digits: You win $3,000!")

elif (gDigit1 == lDigit1 or gDigit1 == lDigit2 or
      gDigit2 == lDigit1 or dDigit2 == lDigit2):
    print("Match One Digit: You win $1,000!")
else:
    print("Sorry, Better luck next time")

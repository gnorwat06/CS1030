#Description: reworking the lottery example
#The winning rules will stay the same

#import the random module
import random

#generate a lottery number with two digits
lottery = str(random.randint(0,9)) + str(random.randint(0,9))
#print(lottery)

#Prompt the user to input their numbers
guess = input("Enter your lottery pick (2 digits): ")

#Display winning number
print(f"The lottery number number is {lottery}")

#Check the guess against the winning cases
if guess == lottery:
    print("Exact Match: You win $10,000!")
elif guess[1] == lottery[0] and guess[0] == lottery[1]:
    print("Matched all digits: You win $5,000!")
elif guess[0] == lottery[0] or guess[0] == lottery[1] or guess[1] == lottery[0] or \
     guess[1] == lottery[1]:
    print("Match one digit: You win $1,000!")
else:
    print("Better Luck Next Time.")

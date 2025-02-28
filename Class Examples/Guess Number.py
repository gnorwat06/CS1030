#Descritption: Randomly generate a number to guess

#import random
import random

#Generate random number to be guessed
num = random.randint(0,100)
print(num)
#Display the prompt message
print("Guess a magic nmber between 0 and 100")

#Create a variable to gain access into our while loop
guess = -1

#create a while loop to iterate until we guess the correct number
while guess != num:
    #Prompt the user to guess the number
    guess = int(input("Enter your guess: "))

    #Create a multiway to let the user know if they got it right
    if guess == num:
        print(f"Yes, the number is {num}")
    elif guess > num:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

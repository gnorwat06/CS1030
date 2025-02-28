#Gavin Norwat
#700746314
#Assignment 7 / Problem 29
#Description: Game: Hangman
#Import random
import random

#Create a main function
def main():

    #Create a list that stroes possible words to be picked from
    words = ["write","program","that"]

    #Create a while loop to play the game until the user opts out
    while True:

        #randomly select the index for the word
        index = random.randint(0,len(words) - 1)

        #Store off that word into a new variable
        hiddenWord = words[index]

        #Using the length function to blurr the word
        guessedWord = len(hiddenWord) * ['*']

        #Track the number of correct and incorrect guesses
        numOfCorrectGuesses = 0
        numOfMisses = 0

        #Set up a while loop where the loop control lets you make unilimited
        #guesses until you get the corrrect word
        while numOfCorrectGuesses < len(hiddenWord):

            #Prompt the user to guess a single letter / invoke string function
            letter = input(f"(Guess) Enter a letter in word {toString(guessedWord\
)}: ").strip()

            #Check if our letter guess is in the word that we randomly select
            if letter in guessedWord:
                #display helpful hint if you already piced that letter
                print(f"\t{letter} is already in the word")

            #check for if the letter is not in the word
            elif hiddenWord.find(letter) <0:
                #display helpful hint if the letter isnt in the word
                print(f"\t{letter} is not in the word")

                #increment number of misses
                numOfMisses += 1

            else:
                k = hiddenWord.find(letter) #finds the index of the letter
                while k >= 0:
                    #reveal the letter
                    guessedWord[k] = letter

                    #increment our correct guesses
                    numOfCorrectGuesses += 1

                    #check the remainding word for the same letter
                    k = hiddenWord.find(letter, k + 1)

        print(f"The word is {hiddenWord}. You missed {numOfMisses}" +
              (" time" if ( numOfMisses <= 1) else " times"))

        #Prompt the user if they want to play again
        anotherGame = input("\nDo you want to guess for another word? \
Enter y/Y or n/N: ").upper()

        #check the user response
        if anotherGame == "N":
            print("\nFinished")
            break

#creating a funciton to strip our list to a string
def toString(list):
    #Create an empty string
    s = ''
    #iterate through the list placing each letter into our empty string
    for i in list:
        s += i

    #return the string back to the caller
    return s

#invoke the main function
main()

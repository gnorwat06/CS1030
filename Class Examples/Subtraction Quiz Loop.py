#Description: Create a math quiz that has 5 questions

#import time and random module
import time, random

#Count the number of correct answers
correctCount = 0

#Count the number of total questions
count = 0

#Name constant to set the limit of the number of questions
NUM_OF_QUESTIONS = 5

#Start the test time
startTime = int(time.time())

#Create a while loop to generate the 5 random questions
#while count < NUM_OF_QUESTIONS:

answer = 'Y'

#user conffirmation demo
while answer == 'Y':

    #1. Generate two random single digit integeres
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    #2. if num1 is less than num2 we need to swap values
    if num1 < num2:
        num1,num2 = num2,num1

    #3. Prompt the student to answer the question
    answer = int(input(f"what is {num1} - {num2}? "))

    #4. Grade the answer an display the results
    if answer == num1 - num2:
        print("You are Correct!")
        #increment the correct count by 1
        correctCount += 1

    else:
        print(f"Your answer is wrong. \n" +
              f"{num1} - {num2} = {num1 - num2}")
    #Increment the count to control the l.c.c
    count += 1

    #Prompt the user to see if they want another question
    answer = input("Would you like another question (n/N) or (y/Y): ").upper()

#Stop the time
endTime = int(time.time())

#Get the total time it otok to take the quiz
testTime = endTime - startTime

#Display the quiz results
print(f"Correct count is {correctCount} / {count}\n" +
      f"Test time is {testTime} seconds")








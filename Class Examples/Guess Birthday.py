#Description: Set of 5 questions which will determine the day you were born

#Birthday to be determined
day = 0

#Prompt the user to answer the first question
question1 = "Is your birthday in Set 1?\n" \
            "01 03 05 07\n" + \
            "09 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question1)

#Check the user response
if answer.upper() == 'Y':
    day += 1

#Prompt the user to answer the second question
question2 = "Is your birthday in Set 2?\n" \
            "02 03 06 07\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question2)

#Check the user response
if answer.upper() == 'Y':
    day += 2

#Prompt the user to answer the third question
question3 = "Is your birthday in Set 3?\n" \
            "04 05 06 07\n" + \
            "12 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question3)

#Check the user response
if answer.upper() == 'Y':
    day += 4

#Prompt the user to answer the fourth question
question4 = "Is your birthday in Set 4?\n" \
            "08 09 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question4)

#Check the user response
if answer.upper() == 'Y':
    day += 8

#Prompt the user to answer the fifth question
question5 = "Is your birthday in Set 5?\n" \
            "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31\n" + \
            "Enter n/N for No and y/Y for Yes: "
answer = input(question5)

#Check the user response
if answer.upper() == 'Y':
    day += 16

#Display the results
print(f"\nYour Birthday is {day}")

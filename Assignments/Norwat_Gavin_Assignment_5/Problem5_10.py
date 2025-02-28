#Gavin Norwat
#700746314
#Assigment 5 / problem 5.10
#Description: display highest name and score.

#Initalize score
highScore = 0
#prompt user for number of students
numStudents = int(input("Enter the number of students: "))

#create a loop to ask the name and scores
for i in range(1,numStudents + 1):

    #Ask for the students score and name
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))

    #check to see if score entered is greater than the highest score so far
    if score > highScore:

        #Set the score to the new highscore and save their name
        highScore = score
        highestScoreName = name

#Print the results
print(f"Top student {highestScoreName}'s score is {highScore}")

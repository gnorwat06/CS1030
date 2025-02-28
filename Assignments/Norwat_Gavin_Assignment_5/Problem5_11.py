#Gavin Norwat
#700746314
#Assigment 5 / problem 5.11
#Description: Find the top two scores the students

#Initalize variables
topScore = -1
secondScore = -2

#Prompt the user for number of students
numStudents = int(input("Enter the number of students: "))

#Create a loop to ask for the scores and names of the students
for i in range(1,numStudents + 1):

    #Ask for score and names
    name = input("Enter a student name: ")
    score = float(input("Enter a student score: "))

    #Check score to determine top and second score
    if score > topScore:
        if topScore > 0 and score > topScore:
            secondName = topName
            secondScore = topScore

        topScore = score
        topName = name
        
    elif score > secondScore and score < topScore:
        secondScore = score
        secondName = name
    
#Print Results
print(f'''Top two students: 
{topName}'s score is {topScore} 
{secondName}'s score is {secondScore}''')
      
            
            

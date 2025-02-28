#Gavin Norwat
#700746314
#Assignment 7 / Problem 7.1
#Description: Read list of scores and grade based on curve

# Prompt the user to enter scores
input_scores = input("Enter scores separated by spaces from one line: ")
scores = [float(score) for score in input_scores.split()]

# Determine the highest score as the best score
best = max(scores)

# Grade each score based on the scheme
index = 0  # Initialize a counter variable for the index
for score in scores:
    if score >= best - 10:
        grade = "A"
    elif score >= best - 20:
        grade = "B"
    elif score >= best - 30:
        grade = "C"
    elif score >= best - 40:
        grade = "D"
    else:
        grade = "F"
    print(f"Student {index} score is {score} and grade is {grade}")
    index += 1  # Increment the index for each student

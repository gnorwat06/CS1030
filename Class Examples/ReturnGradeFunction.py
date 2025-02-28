#Description: Example of a return type function

#return the grade from the score that gets passed in
def getGrade(score):

    #None special value to give control back to the caller
    if score < 0 or score > 100:
        print("Invalid Score")
        return None

    #Check the score for its letter
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Create the main function
def main():

    #Prompt the user to input a score
    score = int(input("Enter a score: "))

    #Display the results / invoke the get grade function
    print(f"The letter grade is {getGrade(score)}")

#Invoke main
main()

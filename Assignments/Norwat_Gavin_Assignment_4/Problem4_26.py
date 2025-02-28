#Gavin Norwat
#700746314
#Assignment 4 / Problem4.26
#Description: determine major and status from user input

#Prompt user for input
user = input("Enter two characters: ")

#determine major and year
major = user[0]
year = user[1]

#print major
match major:
    case 'M':print("Matchematics")
    case 'C':print("Computer Science")
    case 'I':print("Information Technology")
#print year
match year:
    case '1':print("Freshman")
    case '2':print("Sophomore")
    case '3':print("Junior")
    case '4':print("Senior")

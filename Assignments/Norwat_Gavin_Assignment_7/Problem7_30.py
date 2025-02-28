#Gavin Norwat
#700746314
#Assignment 7 / Problem 30
#Description: Chinese zodiac with list
#Prompt the use to input a value for year
year = int(input("Enter a year: "))

lst = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit",
        "Dragon", "Snake", "Horse", "Sheep"]
#Create a match-case statement to determine the animal
match year % 12:
    case 0: print(lst[0])
    case 1: print(lst[1])
    case 2: print(lst[2])
    case 3: print(lst[3])
    case 4: print(lst[4])
    case 5: print(lst[5])
    case 6: print(lst[6])
    case 7: print(lst[7])
    case 8: print(lst[8])
    case 9: print(lst[9])
    case 10: print(lst[10])
    case 11: print(lst[11])
    case _: print("No animal found")

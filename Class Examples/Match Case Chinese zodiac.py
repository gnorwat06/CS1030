#Using the match case to rework the chinese zodiac problem


#Prompt the use to input a value for year
year = int(input("Enter a year: "))

#Create a match-case statement to determine the animal
match year % 12:
    case 0: print("Monkey")
    case 1: print("Rooster")
    case 2: print("Dog")
    case 3: print("Pig")
    case 4: print("Rat")
    case 5: print("Ox")
    case 6: print("Tiger")
    case 7: print("Rabbit")
    case 8: print("Dragon")
    case 9: print("Snake")
    case 10: print("Horse")
    case 11: print("Sheep")
    case _: print("No animal found")

#Description: Write a program to find out the chinese zodiac sign for a given year

#Prompt the user to input a value for the year
year = int(input("Enter a year: "))

#compute the sign with the given formula
sign = year % 12

#Create a multi-way if statement to find the animal
if sign == 0:
    print("Monkey!")
elif sign == 1:
    print("Rooster!")
elif sign == 2:
    print("Dog!")
elif sign == 3:
    print("Pig!")
elif sign == 4:
    print("Rat!")
elif sign == 5:
    print("Ox!")
elif sign == 6:
    print("Tiger!")
elif sign == 7:
    print("Rabbit!")
elif sign == 8:
    print("Dragon!")
elif sign == 9:
    print("Snake!")
elif sign == 10:
    print("Horse!")
else:
    print("Sheep!")

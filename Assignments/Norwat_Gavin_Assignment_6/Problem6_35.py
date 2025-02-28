#Gavin Norwat
#700746314
#Assignment 6 / Problem 6_35
#Description: generate 10,000 uppercase letters and count the occurrences of A

#Import custom random character module
from RandomCharacter import *

#Initialize count
count = 0

#create the loop
for i in range(10000):

    #Generate a letter 
    letter = getRandomUpperCaseLetter()

    #if the letter is A increase the count by 1
    if letter == 'A':
        count +=1

#print the number of times A occurs
print(count)
    
    

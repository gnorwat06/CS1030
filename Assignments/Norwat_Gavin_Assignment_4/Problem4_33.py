#Gavin Norwat
#700746314
#Assignment 4 / Problem4.33
#Description: print three random letters

#import random
import random

#Generate three random digits to convert to letters
'''
ASCII A-Z value 65-90
'''
number1 = random.randint(65, 90)
number2 = random.randint(65, 90)
number3 = random.randint(65, 90)

#Convert ASCII code to letters
letter1 = chr(number1)
letter2 = chr(number2)
letter3 = chr(number3)

#Print the results
print(f"{letter1}{letter2}{letter3}")

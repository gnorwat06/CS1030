#Gavin Norwat
#700746314
#Assigment 5 / problem 5.6
#Description: conversion from miles to kilometeres and kilometers to miles

#Note: 1 miles is 1.609 Kilometers
'''
Miles       Kilometers  |  Kilometers      Miles
11          12          3  16              6
-------------------------------------------------
1           1.609       |  20              12.430
'''

#Display the column headings
print(f"{'Miles':11s}{'Kilometers':12s}{'|':3s}{'Kilometers':16s}{'Miles':6s}")
print('-' * 48)

#Initalize variables
miles = 1
kilometers = 20

#Create a loop that stops after 10 iterations
for i in range(1,10 + 1):
    print(f"{miles:<11d}{miles * 1.609:<12.3f}{'|':3s}{kilometers:<16d}\
{kilometers / 1.609:<6.3f}")

    #Increment variables
    miles += 1
    kilometers += 5

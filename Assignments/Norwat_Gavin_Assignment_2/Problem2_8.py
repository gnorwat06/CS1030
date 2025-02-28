#Gavin Norwat
#700746314
#Assignment 2 / Problem 2.8
#Description: Calculate the energy needed to heat water up
#             from an initial temp to a final temp

'''
Step1: Obtain mass of water, initial temp, and final temp
Step2: use Q = M * (finalTemp - initialTemp) * 4184 to calculate the energy needed
Step3: Display results
'''

#step1:
M = float(input("Enter amount of water in kilograms: "))
initialTemp = float(input("Enter the initial temperature in celsius: "))
finalTemp = float(input("Enter the final temperature in celsius: "))

#Step2:
Q = M * (finalTemp - initialTemp) * 4184

#Step3:
print("The energy needed is", Q, "Joules")

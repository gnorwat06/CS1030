#Gavin Norwat
#700746314
#Assignment 2 / Problem 2.7
#Descrption: Find the number of years and days.

'''
Step1: obtain amount of minutes from user
step2: calculate the amount of years and days from that amount
    a) divide initial amount by 525600 since there are that many minutes in a year.
    b) divide remainder by 1440 since there are that many minutes in a day.
step3: display results
'''

#Step 1:
minutes = int(input("Enter the number amount of minutes: "))

#Step 2:
years = minutes // 525600
minutesRemaining = minutes % 525600

days = minutesRemaining // 1440

#Step 3:
print(minutes, "minutes is approximately",years, "years and", days, "days")
            

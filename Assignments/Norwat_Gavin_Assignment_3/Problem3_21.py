#Gavin Norwat
#700746314
#Assignment 3 / Problem 3.21
#Description: Determind day of week from year, month, and day of month
'''
Step1: prompt user for year,month,and day of month
Step2: compute day of week
Step3: display results
'''

#step1:
year = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day = int(input("Enter the day of the month: "))

#convert 1 and 2 to 13 and 14 of previous year:
if month == 1 or month ==2:
    month += 12
    year -= 1
#print(year,month,day)

#step2:
#k = year of centruy
k = year % 100
#j = year / 100
j = year // 100
dayOfWeek = (day +((26 * (month + 1))//10) + k + (k//4) + (j//4) + (5 * j)) % 7
#print(dayOfWeek)

#step3:
if dayOfWeek == 0:
    print("Day of the week is Saturday.")
elif dayOfWeek == 1:
    print("Day of the week is Sunday.")
elif dayOfWeek == 2:
    print("Day of the week is Monday.")
elif dayOfWeek == 3:
    print("Day of the week is Tuesday.")
elif dayOfWeek == 4:
    print("Day of the week is Wednesday.")
elif dayOfWeek == 5:
    print("Day of the week is Thursday.")
elif dayOfWeek == 6:
    print("Day of the week is Friday.")

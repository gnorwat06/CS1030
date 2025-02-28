#Gavin Norwat
#700746314
#Assignment 3 / Problem 3.20
#Description: Compute wind chill index
'''
step1: obtain temperature and wind speed from user
step2: see if answers are valid if they are not end the program
Step3: Display results
'''
#import system
import sys
#step1:
temp = float(input("Enter the temperature in Fahrenheit: "))
windSpeed = float(input("Enter the wind speed miles per hour: "))

#step2:
if windSpeed <= 2 and temp < -58 or temp > 41:
    print("Temperature and windspeed is invalid")
    sys.exit()
elif temp < -58 or temp > 41:
    print("Temperature is invalid")
    sys.exit()
elif windSpeed <= 2:
    print("Wind speed is invalid")
    sys.exit()

#Step 3:
print(f"The wind chill index is {35.74 + (0.6215 * temp) - (35.75 * (windSpeed ** .16)) + (.4275 * (temp * (windSpeed ** .16

#Gavin Norwat
#700746314
#Assignment 2 / Problem 2.9
#Description: Determine the wind-chill temperature

'''
Step1: obtain the temp and wind speed
Step2: determine the wind-chill temp
Step3: Display results
'''

#Step1:
temp = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
windSpeed = float(input("Enter the wind speed miles per hour (must be greater than or equal to 2): "))

#Step2:
windChill = 35.74 + (0.6215 * temp) - (35.75 * (windSpeed ** .16)) + (.4275 * (temp * (windSpeed ** .16)))

#Step3:
print("The wind chill index is", windChill)

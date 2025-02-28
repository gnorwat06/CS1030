#Description: Computing and interpreting BMI for people 16 or older
'''
conversions
note: 1 pound is 0.45359237 kilograms
note: 1 inch is 0.0254 meters
'''
#name constants for our conversion value
KILO_POUND = 0.45359237
METERS_INCH = 0.0254

#Prompt the user to enter their weight in pounds
weight = float(input("Enter weight in pounds: "))

#Prompt the user to enter the height in inches
height = float(input("Enter the height in inches: "))

#Compute the BMI after the conversions 
weightInKilograms = weight * KILO_POUND
heightInMeters = height * METERS_INCH

bmi = weightInKilograms / (heightInMeters ** 2)

#Display the results using a multi-way
print("BMI is:", round(bmi,2))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

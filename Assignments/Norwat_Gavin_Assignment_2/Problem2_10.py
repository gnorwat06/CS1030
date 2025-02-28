#Gavin Norwat
#700746314
#Assignment 2 / problem 2.10
#Description: Compute the minimum runway length needed for an airplane to take off.

'''
Step1: Obtain speed and acceleration
Step2: compute length of runway
Step3: display results
'''

#Step1:
speed = float(input("Enter speed: "))
acceleration = float(input("Enter acceleration: "))

#Step2:
length = (speed * speed) / (2 * acceleration)

#Step3:
print("The minimum runway length for this airplane is", length, "meters")

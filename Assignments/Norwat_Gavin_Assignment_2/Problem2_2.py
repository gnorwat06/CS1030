#Gavin Norwat
#700746314
#Assignemtn 2 / problem 2.2
#Description: compute the area and volume of a cylinder

#Step 1: Obtain the radius and length of the cylinder
radius = float(input("Enter the radius of a cyliner: "))
length = float(input("Enter the length of a cyliner: "))

#Step 2: Compute the area and volume of the cylinder
area = radius * radius * 3.14159
volume = area * length

#Step 3: Display results
print("The area of the cylinder is",area)
print("The volume of the cylinder is",volume)

#Description: Examples on default, positional, and keyword arguments

#Create a function to display the area
def printArea(width = 1, height = 2):
    area = width * height
    print(f"Width: {width} | Height: {height} | Area: {area}")

#Invoke the printArea with different types of arguments
printArea() #Default args
printArea(4,3) #Positional args
printArea(height = 5) #mix bbetween keyword and default
printArea(width = 2) #Mixed between keyword and default
printArea(2) #Positional mixed with the default

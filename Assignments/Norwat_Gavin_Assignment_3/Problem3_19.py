#Gavin Norwat
#700746314
#Assignment 3 / Problem 3.19
#Description: compute the perimeter of a triangle
'''
Step1: Obtain three edges of a triangle from the user.
Step2: Determine if they are valid answers and display results.
'''

#Step1:
edge1 = float(input("Enter edge 1: "))
edge2 = float(input("Enter edge 2: "))
edge3 = float(input("Enter edge 3: "))

#step2:
if edge1 + edge2 > edge3 and edge2 + edge3 > edge1 and edge1 + edge3 > edge2:
    print(f"The perimeter is {edge1 + edge2 + edge3}")
else:
    print("The input is invalid")
    


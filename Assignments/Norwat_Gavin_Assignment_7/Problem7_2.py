#Gavin Norwat
#700746314
#Assignment 7 / Problem 7.2
#Description: Reverse the order in which numbers were entered

#Hint: You need to take the user input as a sting

#Prompt the user to input numbers separated by 1 space
s = input("Enter numbers separated by sapces from one line: ")
items = s.split() #extracts items from the string

#L.C to comvert the string elements to integers
numbers = [int(x) for x in items]

#Reverse method to reverse the order
numbers.reverse()

#Display the results
print("The reversed list is", end = ' ')

#for loop to iterate through the list and print each element
for i in numbers:
    print(i, end = ' ')

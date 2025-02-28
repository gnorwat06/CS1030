'''
Creating Lists
The elements in a list are separated by commas.
List area enclosed by a pair of square brackets []
Lists can contain the elements of the same or mixed data types
Lists are mutable (contents can be changed)
Lists grow and shrink on demand
'''
#Import the random module
from random import *

#Create an empty list
list1 = []
print(type(list1),list1)

#Create a list of 10 elements with the starting value of 0
list1 = [0] * 10
print(list1)

#Create a lists of integers
list2 = [1,2,3,4,5]
print(type(list2),list2)

#Create a list of strings
list3 = ["red", "green", "blue"]
print(list3)

#We can have any element data type
list4 = [3, True, 3.5, "Hello"]
print(list4)

#List() function creates a list object
#Syntax: list(iterable)
#Note: In python, iterable means an object can be used in iteration

#Create an empty list
list5 = list()
print(list5)

#list6 = list(1,2,3,4,5) No Go

list6 = list([1,2,3,4,5])
print(list6)

list7 = list(range(2,12,2))
print(list7)

list8 = list('ababa')
print(list8)

#Built-in Functions
#len, max, min, sum, shuffle

#len() function returns the number of elements in the list
list1 = [2,3,4,1,22]
print(f"Length of the list is {len(list1)}")

#Max() function returnts the largest element
print(f"Max value in our list is {max(list1)}")

#min() function returns the smallest element
print(f"Min value in our list is {min(list1)}")

#Sum() funciton to add all the element values togeather
print(f"The sum of all elements is {sum(list1)}")

#Shuffle() will shuffle the elemtns randomly in the list
#shuffle(list1)
#print(list1)

#Index Operator []
#An element in a list can be accessed through the index operator
#Syntax: myList[index]
#Note: Indices range from 0 to the len(myList) - 1

myList = [5.6,4.5,3.3,13.2,4.0,34.33,34.0,45.45,99.99]

#myLIst[index] can be used just like a varaible
myList[2] = myList[1] + myList[0]
print(myList)

#You can also iterate through a list
for i in range(len(myList)):
    #Change the element to its current index value
    myList[i] = i
    print(f"Current iteration: {i} | MyList[{i}] value is {i}")
print()
print(myList)

#Python allows for negative numbers as indices to reference positions relative
#to the end of the list
print(list1[-1]) #Note the last index starts at -1
print(myList[-3])

#List slicing [start index : ending index - 1: step value]
#Note: if the start index is left empty it defaults to 0
#Note: if the end index is empty it defaults to the len(list) -1
list1 = [1,3,5,7,9,11]
print(list1[2:4]) #Start at index 2 and end at index 3
print(list1[:5:2])
print(list1[3:])
print(list1[-4:-2])

#You can assign values to a slice of a list
list1[1:4] = [91,92,93]
print(list1)

#The +,*, in and not in
list1 = [1,2]
list2 = [3,4]

#Create a list by concatenation list1 and list2 togeather
list3 = list1 + list2
print(list3)

#Concatenationg the same list n times
list4 = list3 * 3
print(list4)

















#Gavin Norwat
#700746314
#Assignment 7 / Problem 5
#Description: Find and display the distince numbers in the user input

#Create a main function
def main():

    #Prompt the user to input values on one line
    s = input("Enter ten numbers: ")
    items = s.split() #Extracts items from the string
    list1 = [int(x) for x in items] #Convert our elements to integers

    #Create a empty list to store our distinct numbers
    list2 = []

    #Create a for loop to iterate through list1
    for number in list1:
        if not(number in list2):
            #append the distince number
            list2.append(number)

    #display the length and the numbers
    print(f"The number of disinct numbers is {len(list2)}")
    print("The distince numbers are:", *list2)

    #or
    print("The distinct numbers are: ", end = '')
    for number in list2:
        print(number, end = ' ')

#invoke the main function
main()

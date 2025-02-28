#Description: The program will exit when the user types 0 (Sentinel value)

#Prompt the user to input a integer
data = int(input("Enter an integer (Exit upon 0): "))

#Create a while loop to iterate until we input 0
total = 0

while data != 0:

    #add the input value into the total
    total += data

    #reprompt the user to input the next value
    data = int(input("Enter an integer (Exits upon 0): "))

#Display the results
print(f"The sum is {total}")

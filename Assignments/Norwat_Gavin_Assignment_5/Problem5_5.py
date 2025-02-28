#Gavin Norwat
#700746314
#Assigment 5 / problem 5.5
#Description converstion from kilograms to pounds and pounds to kilograms

#Note: 1 pound is .4545 kilograms
#Note: 1 kilogram is 2.2 pounds

#Display the column headings
print(f"{'Kilograms':12s}{'Pounds':10s}{'|':6s}{'Pounds':12s}\
{'Kilograms':12s}")
print('-' * 55)

#Initalize variables
kilograms = 1
pounds = 20

#create a for loop stop our iteration at 199
for i in range(1,200,2):
    print(f"{kilograms:<12d}{kilograms * 2.2:<10.1f}{'|':6s}\
{pounds:<12d}{pounds * .4545:<12.2f}")

    #Increment kilograms by 2 and pounds by 5
    kilograms += 2
    pounds += 5

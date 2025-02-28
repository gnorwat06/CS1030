#Gavin Norwat
#700746314
#Assignment 5 / Problem 5.3
#Description: Conversion from kilograms to pounds
#Note 1 kilo = 2.2 pounds
'''
Kilograms   Pounds
1              2.2
3              6.6
'''

#Display the headings
print(f"{'Kilograms':12s}{'Pounds':>10s}")
print('-' * 22)

#Create a for loop to iterate until it hits 199
for kilograms in range(1,200,2):

    #Display the conversion
    print(f"{kilograms:<12d}{kilograms * 2.2:>10.1f}")

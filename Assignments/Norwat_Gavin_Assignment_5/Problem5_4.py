#Gavin Norwat
#700746314
#Assignment 5 / Problem 5.4
#Description: Coversion from miles to kilometers
#Note: 1 mile = 1.609 kilometers
'''
Miles       Kilometers
1           1.609
2           3.218
'''

#Display the headings
print(f"{'Miles':12s}{'Kilometers':10s}")
print('-' * 22)

#Create a loop to iterate unitl it hits 10
for miles in range(1,10 + 1):

    #Display the conversion
    print(f"{miles:<12d}{miles * 1.609:<10.3f}")

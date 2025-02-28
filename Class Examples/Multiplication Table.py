#Display the title
print(f"{'Multiplication Table':>30s}")
print("-" * 40)

#Display the number
print("   ", end = '')

#Create a for loop to display the column numbers
for i in range(1,10):
    print(f"{i:4d}", end = '')
print() #jump to new line
print("-" * 40)

#Display the table body
#i is going to be the outer loop which you can
#think of as in rows. j is going to be our inner loop which is you can think of
#as columns
#Note: For every iteration of I you will exhaust all iteration of j
for i in range(1,10):
    print(i,"|", end = '')
    for j in range(1,10):
        #display the product and alignment
        print(f"{i * j:4d}", end = '')

    print()#Jump to the next row

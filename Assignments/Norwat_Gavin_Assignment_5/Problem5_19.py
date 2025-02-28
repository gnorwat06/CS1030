#Gavin Norwat
#700746314
#Assigment 5 / problem 5.19
#Description: Display a pyramid

#Get the amount of lines from the user
n = int(input("Enter the number of lines: "))

#Create the main loop to iterate the amount of times specified by the user
for i in range(1, n + 1):
    #print the leading spaces
    print('   ' * (n - i), end='')

    #print the left side
    for j in range(i, 0, -1):
        print(f'{j:2}', end=' ')

    #print the right side
    for j in range(2, i + 1):
        print(f'{j:2}', end=' ')

    #move to next line
    print()

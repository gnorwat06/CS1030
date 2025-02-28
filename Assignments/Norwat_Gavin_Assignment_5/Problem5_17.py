#Gavin Norwat
#700746314
#Assigment 5 / problem 5.17
#Description: Display the ASCII character table with 10 characters per line

#initalize variables
start = 33
end = 126
chars_per_line = 10

#Create a loop to convert each character within the range

for i in range(start, end +1):
    print(chr(i), end=' ')
    
    #Print newline every 10 characters
    if (i - start + 1) % chars_per_line == 0:
        print()

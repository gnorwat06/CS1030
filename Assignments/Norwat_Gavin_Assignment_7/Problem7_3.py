#Gavin Norwat
#700746314
#Assignment 7 / Problem 7.3
#Descriptoin: count the occurences of numbers in a list

# Prompt the user to enter integers between 1 and 100
input_numbers = input("Enter the integers between 1 and 100: ")

# Convert the input into a list of integers
numbers = [int(num) for num in input_numbers.split()]

# Initialize a list to hold counts for each number from 1 to 100
counts = [0] * 100  # List of 100 zeros, one for each possible integer

# Count occurrences of each number in the input
for number in numbers:
    if 1 <= number <= 100:  # Only count numbers within the range
        counts[number - 1] += 1  # Increment the count at the index (number - 1)

# Display the results
for i in range(100):
    if counts[i] > 0:
        print(f"{i + 1} occurs {counts[i]} time{'s' if counts[i] > 1 else ''}")

#Gavin Norwat
#700746314
#assignment 7 / Problem 7.7
#Description: count single digits

#import random
import random

# Create a list of 10 elements initialized to 0 to store counts for digits 0 to 9
counts = [0] * 10

# Generate 1,000 random integers between 0 and 9 and update the counts
for _ in range(1000):
    num = random.randint(0, 9)
    counts[num] += 1

# Display the count for each number
for i in range(10):
    print(f"Count of {i}s: {counts[i]}")

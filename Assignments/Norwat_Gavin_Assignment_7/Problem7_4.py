#Gavin Norwat
#700746314
#Assignment 7 / Problem 7.4
#Description: determine average, below average, and above average

        # Get input from the user and split it into a list of integers
input_data = input("Enter the numbers: ")
scores = [int(x) for x in input_data.split()]

# Calculate the average score
if scores:
    average = sum(scores) / len(scores)
    print(f"Average is {average:.1f}")

    # Count scores above or equal to the average and below the average
    above_or_equal = sum(1 for score in scores if score >= average)
    below = sum(1 for score in scores if score < average)

    print(f"Number of scores above or equal to the average is {above_or_equal}")
    print(f"Number of scores below the average is {below}")
else:
    print("No scores entered.")

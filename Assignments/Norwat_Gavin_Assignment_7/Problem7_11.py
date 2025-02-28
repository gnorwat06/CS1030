#Gavin Norwat
#700746314
#assignment 7 / problem 7.11
#description: Create a custom shuffle function
import random

def shuffle(lst):
    # Shuffle the list by swapping elements randomly
    for i in range(len(lst)):
        # Pick a random index to swap with
        j = random.randint(0, len(lst) - 1)
        # Swap elements at indices i and j
        lst[i], lst[j] = lst[j], lst[i]

def main():
    # Main program to test the shuffle function
    input_data = input("Enter numbers: ")
    # Convert input string to a list of floats
    lst = [float(x) for x in input_data.split()]

    # Shuffle the list
    shuffle(lst)

    # Display the shuffled list
    print(lst)

main()

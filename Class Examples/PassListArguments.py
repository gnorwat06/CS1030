#Create the main functin
def main():
    x = 1 #x represents an integer object (Immutable object)
    y = [1,2,3] #y represents a list object (Mutable object)

    #invoke the m fuunction with x and y arguments
    m(x,y)

    #Display the results after the funtion is done
    print(f"Value of x: {x}")
    print(f"Value of y[0]: {y[0]}")

#Create a function to change the value of the integer and list
def m(number,numbers):
    number = 1001 #assign a new value to number
    numbers[0] = 5555 #index 0 will get a new value

#invoke the main function
main()

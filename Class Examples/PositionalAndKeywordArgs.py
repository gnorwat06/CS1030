'''
Two kinds of arguments: positional and keyword arguments

Positional: Will be passed in the same order as their respective formal
parameters in the function header

Keyword: Can appear in any order as you are assigning the value to the formal
parameters

Note/Warning: you can mix these types: Positional will come before any
keyword argument
'''

#Function to display a message n times
def print_message(message,n):

    #Create a for loop to iterate n times
    for i in range(n):
        #Display the message
        print(message)

#Invoke the print_message function and pass positional / keyword args
print_message("Welcome to Python", 5)
#print_message(5,"Hello, World")
print_message(n = 5, message = "Hello, World")
print_message("Python", n = 5)
#print_message(n = 2, "Python")

#Description: For loop example

#Iterating through a sequence. A string is a sequence of characters. So are lists
#and tuples. Also known as sequence-type objects

#The varaible i takes on each successive value in the sequence
j = 0
for i in "Apple":
    print(f"Itteration: {j}  | Element: {i}")
    j += 1
print("\n")

#The function range(a,b - 1) returns a sequence of integers
#Note / Warning: The range function can only take in INTEGERS
for i in range(4,8):
    print(i)
print("\n")

#The range function has two more versions
#range(b -1)
#Defaults: We will start at zero and increment by 1
for i in range(5):
    print(i, end =' | ')
print("\n")

#range(a,b,k) k is uses as the step value
#The first number in the sequence is (a)
#Each successive number in the sequence will increase by the step value K.
#(b) is the limit (less than)
i = 0
for value in range(3,9,2):
    print(f"Itteration: {i} | Value: {value}")
    i += 1
print("\n")

#Range(a,b,k) function can count backwards if k is a negative value
#The last number in the sequence must be greater than the end value
i = 0
for value in range(50,5,-5):
    print(f"Itteration: {i} | Value: {value}")
    i += 1
print("\n")
    
#If the loop body does not reference the loop variable you can use the underscore
#(_) instead of an explicit variable
for _ in range(3):
    print("Welcome to python")

#Description: Palindorome Example: mom, dad, noon

#Prompt the user to input a string
s = input("Enter string: ")

#The index of the first character in the string
low = 0

#The index of the last character in the string
high = len(s) - 1

#Set isPalindrome to a boolean value
isPalindrome = True

#Create a while loop to iterate until our low index is one a way from our high index
while low < high:
    #If our string at index low and high do not match
    if s[low] != s[high]:
        isPalindrome = False #Not a palindrome
        break #Breaks out of the loop

    low += 1 #Increment low index
    high -= 1 #Drecrement high index

#Two-way if statemnet to display the results
if isPalindrome:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

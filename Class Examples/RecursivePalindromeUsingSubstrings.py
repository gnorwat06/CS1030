'''
Note: A string is a palindrome if it reads the same from the left and from
the right

Examples: mom, dad, kayak, wow, peep

considering if a string is a palindrome can be divided in two sub problems

Problem 1: Determine wheter the first character and the last character of the
string are equal

Problem 2: Ignore the two end characters and see if the rest of the string is
a palindrome

Notice: the second problem is the same as the original problem but smaller
'''
#create a function to check if a string is a palindrom
def isPalindrome(s):

    #base case 1: if the string size is 0 or 1
    if len(s) <= 1:
        return True
    #base case 2: the two end characters are not the same
    elif s[0] != s[len(s) - 1]:
        return False
    #recursive call: string slicing
    #creates a new string which is the same as the original minus the first
    #character and last character
    else:
        return isPalindrome(s[1:len(s) - 1])

#create a main function
def main():

    #Ivoke the isPalindrome function to check words
    print("Is moon a palindrome?", isPalindrome("moon"))
    print("Is noon a palindrome?", isPalindrome("noon"))
    print("Is aba a palindrome?", isPalindrome("aba"))
    print("Is ab a palindrome?", isPalindrome("ab"))
    print("Is peep a palindrome?", isPalindrome("peep"))

#invoke the main
main()

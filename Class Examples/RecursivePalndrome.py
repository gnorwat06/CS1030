'''
This new function is called a recursive helper function. The original
problem can be solved by invoking the recursive helper function.
'''
#Create the is Palindrome function checks wheter a string is a palindrome
def isPalindrome(s):
    #Invoke helper function
    return isPalindromeHelper(s,0,len(s) - 1)

#Helper function
def isPalindromeHelper(s,low,high):

    #Base case 1: We have 1 or no characters left to check
    if high <= low:
        return True

    #Base case 2: First and last characters do not match
    elif s[low] != s[high]:
        return False

    #Recursive call checking the next indices
    else:
        return isPalindromeHelper(s,low + 1, high - 1)

#create the main function
def main():

    #invoke the ispalindrome function
    print("Is moon a palindrome?", isPalindrome("moon"))
    print("Is noon a palindrome?", isPalindrome("noon"))
    print("Is aba a palindrome?", isPalindrome("aba"))
    print("Is python a palindrome?", isPalindrome("python"))

#invoke main
main()

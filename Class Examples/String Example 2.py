#The string class methods are for manipulating strings
#table 4.5 methods for testing its characters
s = "Welcome to python"

#isalnum() returts true if all characters in the string are alaphanumeric and
#there is at least 1 character (a-z)(0-9)
print(s.isalnum())

#isdigit() returns true if the string contains only numbers
print("1234".isdigit())

#islower() returns true if all the letters are all lowercase
print("abc".islower())

#isupper() returns true if all the letters are all uppercase
print("ABC".isupper())

#table 4.6 Methods for searching substrings
#endswith() and startswith() methods
print(s.endswith("thon"))
print(s.startswith("become"))

#find(s) returns the lowest index where the string starts
#rfind(s) returns the largest index where the string is
#Both methods will return -1 if the string is not found
print(s.find("come"))
print(s.rfind("come"))

#Count() returns the number of non-lapping occurrences
print(s.count('o'))

#table 4.7 methods for convertin letter cases in strings
print("WELCOME".lower())
print("welcome".upper())
print("welcome".capitalize())
print("welcome to python".title())
print("WeLcOmE".swapcase())

#Table 4.8 methods for stripping left and right whitespace
s1 = "\tWelcome to Python\t\n"
print(s1.lstrip()) #removes the left whitespace characters
print(s1.rstrip()) #removes the right whitespace characters
print(s1.strip()) #removes both sides whitespace characters


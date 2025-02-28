#description: Determine whether a year is a leap year

#Prompt the user to input a value for year
year = int(input("Enter a year: "))

#Compute if it is a leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#display results
print(f"{year} is a leap year? Answer: {isLeapYear}")


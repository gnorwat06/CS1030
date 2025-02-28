#Gavin Norwat
#700746314
#Assignment 2 / Problem 2.6
#Description: Compute the monetary change of a given amount.

'''
Step1: obtain total
Step2: find ammount for dollar, quarter, nicke, dime, and penny.
    a) divide total by 100 for dollars. dollarRemainder is new total.
    b) divide dollarRemainder by 25 for quarters. quarterRemainder of that is new total.
    c) repeat for dime, nickel, penny.
Step3: Display results.
'''
#Step 1: Obtain value from user.
total = int(input("Enter an amount as integer, e.g., 1156 for 11 dollars 56 cents: "))

#Step 2:
dollarAmount = total // 100 #This amount is the amount of dollars 
dollarRemainder = total % 100 #This is the remaining total after the dollars are taken out

quarterAmount = dollarRemainder // 25
quarterRemainder = dollarRemainder % 25

dimeAmount = quarterRemainder // 10
dimeRemainder = quarterRemainder % 10

nickleAmount = dimeRemainder // 5
nickleRemainder = dimeRemainder % 5

pennyAmount = nickleRemainder // 1

#Step 3:
print("Your amount", total, "consist of:")
print("       ", dollarAmount, "Dollars")
print("       ", quarterAmount, "Quarters")
print("       ", dimeAmount, "Dimes")
print("       ", nickleAmount, "Nickles")
print("       ", pennyAmount, "Pennies")



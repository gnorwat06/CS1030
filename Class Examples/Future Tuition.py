#Description: Predicting the future tuition until the tuition has doubled.
#Note: Tuition for a university is $10,000 dollars this year and will
#increase 7% every year.

#Create a variable to store the starting tuition
tuition = 10000

#Starting at year 0
year = 0

#Create a while loop and set its condition to exit when the tuition is doubled
while tuition < 20000:

    #Compute the interest
    tuition *= 1.07

    #Increment the year
    year += 1

#display the results
print(f"The tuition will be doubled in {year} years.")
print(f"The tuition will be ${tuition:.2f} in {year} years.")

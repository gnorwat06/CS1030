#Gavin Norwat
#700746314
#Assignment 6 / Problem 6.8 
#Description: Convert celsius to farenheight and vise versa using functions

#Convert from celsius to fahrenheit
def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32


#convert from fahrenheit to celsius
def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

#Create main function
def main():
    #Print the header
    print(f"{'celsius':<16s}{'Fahrenheit':<18s}{'|':<6s}\
{'Fahrenheit':<16s}{'Celsius':<7s}")

    print('-' * 63)


    #Initalize variables
    celsius = 40

    fahrenheit = 120
        
    #Create the loop to loop 10 times for each row of the table
    for i in range(10):

        

        print(f"{celsius:<16d}{celsiusToFahrenheit(celsius):<18.2f}{'|':<6s}\
{fahrenheit:<16d}{fahrenheitToCelsius(fahrenheit):<7.2f}")

        #Iterate varaibles
        celsius -= 1

        fahrenheit -= 10

#Invoke main function
main()

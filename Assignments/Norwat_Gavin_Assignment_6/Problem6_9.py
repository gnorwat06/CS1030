#Gavin Norwat
#700746314
#Assignemnt 6 / problem 6.9
#Description: Create a table to convert feet to meters and meters to feet
#Convert from celsius to fahrenheit
def footToMeter(foot):
    return .305 * foot


#convert from fahrenheit to celsius
def meterToFoot(meter):
    return meter / .305

#Create main function
def main():
    #Print the header
    print(f"{'Feet':<16s}{'Meters':<18s}{'|':<6s}\
{'Meters':<16s}{'Feet':<7s}")

    print('-' * 63)


    #Initalize variables
    foot = 1

    meter = 20
        
    #Create the loop to loop 10 times for each row of the table
    for i in range(10):

        

        print(f"{foot:<16d}{footToMeter(foot):<18.3f}{'|':<6s}\
{meter:<16d}{meterToFoot(meter):<7.2f}")

        #Iterate varaibles
        foot += 1

        meter += 5

#Invoke main function
main()

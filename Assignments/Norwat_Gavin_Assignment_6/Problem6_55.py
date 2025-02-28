#Gavin Norwat
#700746314
#Assignment 6 / Problem 55
#Description: Phone keypad where we translate the letters to their respective
#number value

#Create a main functin
def main():
    #Prompt the user to input the phone number as a string
    s = input("Enter a string: ").upper()

    #Iterate through the phone number
    for ch in s:
        #Check to see if our current value (ch) is a letter
        if ch.isalpha():
            #If true invoke the getNumber function
            print(getNumber(ch), end = '')

        else:
            #Its a number character
            print(ch ,end = '')

#Create the getNumber function
def getNumber(uppercaseLetter):

    #Create a match case to find the letter numbe value
    match uppercaseLetter:
        case 'A' | 'B' | 'C': number = 2
        case 'D' | 'E' | 'F': number = 3
        case 'G' | 'H' | 'I': number = 4
        case 'J' | 'K' | 'L': number = 5
        case 'M' | 'N' | 'O': number = 6
        case 'P' | 'Q' | 'R' | 'S': number = 7
        case 'T' | 'U' | 'V': number = 8
        case 'W' | 'X' | 'Y' | 'Z': number = 9

    #return the number back to the caller
    return number

#invoke the main function
main()

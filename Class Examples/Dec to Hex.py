#Description: converting a decimal number to hexadecimal

#Prompt the user to enter a decimal integer
decimal = int(input("Enter a decimal integer: "))

#create a empty string
hex = ''

#Create a while loop to exit when we reach zero
while decimal != 0:

    #Store off the remainder
    hexValue = decimal % 16

    #convert a decimal value to a hex digit character
    if 0 <= hexValue <= 9:
        hexChar = chr(hexValue + ord('0'))

    else:
        hexChar = chr(hexValue - 10 + ord('A'))

    hex += hexChar #adding the character to the empty string

    #Divide 16 by our decimal value
    decimal //= 16

#Display the results
print(f"the hex humber is {hex}")

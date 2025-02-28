#Description: Returning Multiple Values using S.Assignment (chp 2)

#Create a function to sort values in ascending order
def sort(num1,num2):

    #Check to see if num1 is less than num2
    if num1 < num2:
        return num1,num2
    else:
        return num2,num1

#Using S.A to store multiple values
n1,n2 = sort(22,18)

#Display the values of n1 and n2
print(f"N1 = {n1} and N2 = {n2}")

'''
#Create a funciton to append a new value to a list
def add(x,lst = []): #lst is empty by default

    #Check to see if x is in the list
    if x not in lst:
        lst.append(x) #Adding the value to the end of the list

    #Return the lst back to the caller
    return lst
'''
#Default none list
def add(x, lst = None):
    #Check if lst is none
    if lst == None:
        lst = []

    if x not in lst:
        lst.append(x)

    #return back to the caller
    return lst

#Create the main function
def main():

    #invoking the add function to see how default list arguments work
    list1 = add(1)
    print(list1)

    list2 = add(2)
    print(list2)

    list3 = add(3, [11,12,13,14])
    print(list3)

    list4 = add(4)
    print(list4)

#invoke the main function
main()

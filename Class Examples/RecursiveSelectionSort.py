'''
Selection sort: Finds the smallest element in a list
and swaps it with the first element.

Find the smallest element remaining and swap it with the new first element.
'''
#Create the sorst functin
def sort(lst):
    #Invoke the helper function
    sortHelper(lst,0,len(lst) - 1)

#Create the helper function that sorts a sublist
def sortHelper(lst, low, high):

    #Check if low index is still less than the high index
    if low < high:

        #Store off the low index
        indexOfMin = low

        #Create a variable to store the smallest value
        min = lst[low]

        #Iterate through the remaining indices
        for i in range(low + 1, high + 1):
            if lst[i] < min:
                #Store the current lowest value
                min = lst[i]
                indexOfMin = i

        #Swap the smallest in the list
        lst[indexOfMin] = lst[low]
        lst[low] = min

        #recursive call to sort the remainng list
        sortHelper(lst, low + 1, high)

#Define the main function
def main():
    #create an unsorted list of integeres
    lst = [3, 2, 1, 6, 3, 6, 7, 30, 20, 35]

    #invoke the sort function
    sort(lst)

    #Display the sotrted list
    print(*lst)

#invoke the main function
main()

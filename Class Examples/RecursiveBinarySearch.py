'''
Binary Search using recursion

Note: For a binary search to work, the elements in the list must be sorted
'''
#Create the binary search function
def binarySearch(lst, key):

    #invoke the helper function
    return binarySearchHelper(lst, key, 0 , len(lst) - 1)

#create the helper function
def binarySearchHelper(lst,key,low,high):

    #Base case 1: List has been exhausted without a match
    if low > high:
        return -1

    #Find the middle index of the list
    mid = (low + high) // 2

    #Search first half of the list
    if key < lst[mid]:
        #Recursive call to check the remainder of the first half
        return binarySearchHelper(lst,key,low,mid - 1)

    #have a match
    elif key == lst[mid]:
        return mid

    #Check the second half of the list
    else:
        #recursive call to check the remainder of the second half
        return binarySearchHelper(lst,key,mid + 1, high)

#Create a main function
def main():

    #Create a sorted list
    lst = [3, 5, 6, 8, 9, 12, 25, 35, 36]

    #invoke the binarySearchFunction
    print(f"The index of the key: {binarySearch(lst,8)}")
    print(f"The index of the key: {binarySearch(lst,5)}")
    print(f"The index of the key: {binarySearch(lst,22)}")

#invoke the main function
main()

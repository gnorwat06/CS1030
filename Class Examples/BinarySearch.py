'''
Binary Search Algorithm

Note/Warning: Your list must be sorted first before you search

Binary search first compares the key with the element in the middle of the
list.

Cases:
Case 1: If the key is less than the list middle element,  you need to
continue to search only in the first half of the list.

Case 2: If the key is equal to the list middle element, the search ends
with a match.

Case 3: If the key is greater than the list middle element, you need to
continue to search only in the second half of the list.

'''

#Use binary search to find the key i the list
def binarySearch(lst,key):

    #initialize low and high index values
    low = 0
    high = len(lst) - 1

    #While loop and iterate as long as our high index is greater or equal
    #to the low index
    while high >= low:

        #Find the middle index
        mid = (low + high) // 2

        #Check the 3 cases above
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    #Return -1 if the key is not found
    return -1

list1 = [-3,1,2,4,9,23] #Already sorted
print(binarySearch(list1,2))
print(binarySearch(list1,9))
print(binarySearch(list1,22))

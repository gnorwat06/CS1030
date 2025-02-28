'''
Linear Search Algorithm

This search compares the key element key sequentially
with each element in the list

We will search until we find the element or exhausted our list

'''
#The funciton for finding the key in the list
def linearSearch(lst,key):

    #iterate through the list in search for the key
    for i in range(len(lst)):
        if key == lst[i]:
            return i #Returning the current index value

    #Return -1 the key was not found
    return -1

list1 = [4,5,1,2,9,-2,-3]
print(linearSearch(list1,1))
print(linearSearch(list1,9))
print(linearSearch(list1,22))

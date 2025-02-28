'''
The Problem is to find the size of a directory

The size of a directory is the sum of the sizes of all the files
in the directory

We will need to implement three methods out of the OS module

Note: The OS module in Python provides functions for interacting with
the operating system
'''

#import the os module
import os

#create the main function
def main():

    #Prompt the user to enter a directory of file path name
    path = input("Enter a directory or a file: ").strip()

    #invoke getSize / display the total size of the file / direcotry
    ##xception Handling
    #try block lets you test a block of code for errors
    try:
        print(getSize(path), "bytes")
    #Exept block lets you handle the error
    except: 
        print("Directory or file does not exist")

    #you can also use an else block within the exception handling if no
    #errors were raised
    #you can also use a finally block, which will be executed
    #regardless if the try block raises an error or not.
    finally:
        print("Finally executed")

#Create a funciton to get the size of all files
def getSize(path):

    #variable to store the total size of all files
    size = 0

    #If the path is a directory, each sub item (file or subdirectory in the
    #current direcotry is recursively invoke to obtain the size
    if not os.path.isfile(path):
        lst = os.listdir(path) #return a list of all files and subdir
        for subdirectory in lst:
            #Recursive call
            size += getSize(path + "\\" + subdirectory)

    else: #Base case, it is a file
        size += os.path.getsize(path) #accumulate file size

    #Return the size back to the caller
    return size

#invoke the main function
main()

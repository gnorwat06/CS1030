#Description: Counting the occurrence of each letter among 100 letters

#Import the RandomCharacter module
import RandomCharacter

#Create a main function
def main():

    #Create a list of characters
    chars = createList()

    #Display the list
    print("The lowercase letters are: ")
    displayList(chars)

    #Count the occurrence of each letter
    counts = countLetters(chars)

    #Display counts
    print("The occurrences of each letter are: ")
    displayCounts(counts)

#Create a function to generate our list of characters
def createList():
    #Create an empty list
    chars = []

    #Create a for loop to iterate 100 times to get the randomly
    #generated characters
    for i in range(100):
        chars.append(RandomCharacter.getRandomLowerCaseLetter())

    #Return the list back to the caller
    return chars

#create a function to display the list
def displayList(chars):
    #Display the characters in the list 20 per line
    for i in range(len(chars)):
        if (i + 1) % 20 == 0:
            #Print will jump to the new line after it displays the character
            print(chars[i])
        else:
            print(chars[i], end = ' ')

        return chars

def countLetters(chars):
    #Create a new list of 26 integers with the initial value of 0
    counts = 26 * [0]

    #For loop to iterate through the list and increment the index of the current
    #letter
    for i in range(len(chars)):
        counts[ord(chars[i]) - ord('a')] += 1

    #return the count list back to the caller
    return counts

#display the counts of each letter
def displayCounts(counts):
    #Display 10 per line
    for i in range(len(counts)):
        if (i + 1) % 10 == 0:
            #Jump to the next line after we display the number/letter
            print(counts[i], chr(i + ord('a')))
        else:
            print(counts[i], chr(i + ord('a')), end = ' | ')

#invoke the main function
main()
    

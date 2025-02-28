'''
Rule 1: There are n disk labeled 1,2,3 ... n and three towers labeled
towerA, towerB, towerC

Rule 2: No disk can be on top of a smaller disk at any time

Rule 3: All the disks are initially placed on towerA

Rule 4: Only one disk can be moved at a time and it must b e the top disk
'''
#Create a main function
def main():
    #Prompt the user to input the number of disks
    n = int(input("Enter number of disks: "))

    #Find the solution recursivly
    print("The moves are: ")
    moveDisk(n, 'A', 'B', 'C')

#The funciton for finding the solution to move n disk to move from A to B
def moveDisk(n,fromTowerA,toTowerB,auxTowerC):

    #Base Case: We can simply move the disk from A to B
    if n == 1:
        print(f"Move disk {n} from {fromTowerA} to {toTowerB}")

    else:
        #Recursive calls (2): When n > 1 we could split the original problem
        #into three subproblems and sovle them sequentially

        #Move the first n - 1 disk from A to C with the assist of B
        moveDisk(n - 1, fromTowerA, auxTowerC, toTowerB)

        #Move disk n from A to B
        print(f"Move disk {n} from {fromTowerA} to {toTowerB}")

        #Move n - 1 disks from C to B with the assist of A
        moveDisk(n - 1,auxTowerC,toTowerB,fromTowerA)

#invoke the main function
main()

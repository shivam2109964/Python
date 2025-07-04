def printRec(n):
    if(n == 0):
        return
    print(n)
    printRec(n - 1)
    

n = int(input("Enter the n value: "))
printRec(n)

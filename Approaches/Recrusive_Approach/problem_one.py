def printRec(n):
    if(n == 0):
        return
    printRec(n - 1)
    print(f"{n} ")

n = int(input("Enter the n value: "))
printRec(n)
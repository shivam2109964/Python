def sumRec(n):
    if(n == 0):
        return n
    return n + sumRec(n - 1)

value = int(input("Enter the n value: "))
result = sumRec(value)
print(result)
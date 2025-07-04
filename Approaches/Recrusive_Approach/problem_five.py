def powerRec(x , y):
    if(y == 0):
        return 1
    return x * powerRec(x, y - 1)

x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
result = powerRec(x, y)
print(result)

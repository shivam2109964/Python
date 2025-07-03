# Find the Maximum and Minimum Element in an Array

def findMax(array, length):
    max = array[0]
    for i in range(1, length):
        if(array[i] > max):
            max = array[i]
    return max

def findMin(array, length):
    min = array[0]
    for i in range(1, length):
        if(array[i] < min):
            min = array[i]
    return min    

length = int(input("Enter the length of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
max = findMax(array, length)
min = findMin(array, length)
print(f"MAX: {max}, MIN: {min}")
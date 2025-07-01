# Given an array arr. The task is to find the largest element in the given array. 
def largest(array, length):
    max = array[0]
    for i in range(1, length):
        if(array[i] > max):
            max = array[i]
    return max

def findMax(array, index):
    if(index == len(array) - 1):
        return array[index]
    recMax = findMax(array, index + 1)
    return max(recMax, array[index])

def largestRec(array):
    return findMax(array, 0)



length = int(input("Enter the length of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
largestElement = largest(array, length)
print(f"Largest element is: {largestElement}")
result = largestRec(array)
print(f"Largest element by Recursive {result}")
    
def findLargestElement(array, length):
    max = array[0]
    for i in range(1, length):
        if array[i] > max:
            max = array[i]
    return max

def largest(array):
    return findLargestElementRec(array, 0)

def findLargestElementRec(array, i):
    if i == len(array) - 1:
        return array[i]
    
    recMax = findLargestElementRec(array, i + 1)
    return max(recMax, array[i])

array = [45, 78, 96, 48, 21, 46, 35, 28, 71, 65, 84, 92, 64]
length = len(array)
result = findLargestElement(array, length)
print(f"Largest element is: {result}")
resultOne = largest(array)
print(f"Largest element is: {resultOne}")
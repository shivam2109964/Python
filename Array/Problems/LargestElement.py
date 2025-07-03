def findLargestElement(array, length):
    max = array[0]
    for i in range(1, length):
        if array[i] > max:
            max = array[i]
    return max

array = [45, 78, 96, 48, 21, 46, 35, 28, 71, 65, 84, 92, 64]
length = len(array)
result = findLargestElement(array, length)
print(f"Largest element is: {result}")
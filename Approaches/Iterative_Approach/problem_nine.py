def secondLargestElement(array, length):
    largest = secondLargest = float('-inf')
    for i in range(length):
        if array[i] > largest:
            secondLargest = largest
            largest = array[i]
        elif(array[i] > secondLargest and array[i] != largest): 
            secondLargest = array[i]
    if secondLargest == float('-inf'):
        return -1
    return secondLargest
        
length = int(input("Enter the length of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
result = secondLargestElement(array, length)
print(f"The Second Largest Value is: {result}")
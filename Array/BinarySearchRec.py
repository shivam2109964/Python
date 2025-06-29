def insertionSort(array, length):
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        
def binarySearchRef(array, search, low, high):
    if(low > high):
        return -1
    else:
        mid = low + (high - low) // 2
        if(search == array[mid]):
            return mid
        if(search < array[mid]):
            return binarySearchRef(array, search, low, mid - 1)
        else:
            return binarySearchRef(array, search, mid + 1, high)

length = int(input("Enter the legnth: "))
array = [int(input(f"Enter the {i + 1} value: ")) for i in range(length)]
insertionSort(array, length)
print(array)
search = int(input("Enter the element you search for: "))
result = binarySearchRef(array, search, 0, length - 1)
if(result != -1):
    print(f"Match found at index: {result}")
else: 
    print("Match not found.")
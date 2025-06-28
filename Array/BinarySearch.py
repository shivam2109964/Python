def insertionSort(array, length):
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] >= key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
def binarySearch(array, search, low, high):
    while(low <= high):
        mid = low + (high - low) // 2
        if(search == array[mid]):
            return mid
        if(search > array[mid]):
            low = mid + 1
        else:
            high = mid - 1
        
            
length = int(input("Enter the legnth of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
search = int(input("Enter the value you serach for: "))
insertionSort(array, length)
print(array)
result = binarySearch(array, search, 0, length - 1)
if(result != -1):
    print(f"Match found at index: {result}")
else:
    print("Match not found")
def insertionSort(array, length):
    for i in range(1 , length):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def secondLargestEle(array, length):
    for i in range(length - 2, -1 , -1):
        if array[i] != array[length - 1]:
            return array[i]
    return -1

def secondLargestByTwoPass(array):
    length = len(array)
    largest = -1
    secondLargest = -1
    for i in range(length):
        if array[i] > largest:
            largest = array[i]
    for i in range(length):
        if array[i] > secondLargest and array[i] != largest:
            secondLargest = array[i]
    return secondLargest

def secondLargestByOnePass(array):
    length = len(array)
    largest = -1
    secondLargest = -1
    for i in range(length):
        if array[i] > largest:
            secondLargest = largest
            largest = array[i]
        elif array[i] < largest and array[i] > secondLargest:
            secondLargest = array[i]
    return secondLargest
             

array = [10, 10, 10, 2, 10]
insertionSort(array, len(array))
result = secondLargestEle(array, len(array) - 1)
print(f"Second Largest Value is: {result}")
resultTwo = secondLargestByTwoPass(array)
print(f"Second Largest By Two Pass: {resultTwo}")
resultThree = secondLargestByOnePass(array)
print(f"Second Largest By One Pass: {resultThree}")
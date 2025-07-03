def firstRepeatingElement(array, length):
    for i in range(length):
        for j in range(i + 1, length):
            if array[i] == array[j]:
                return i
    return -1

array = [ 10, 5, 3, 4, 4, 3, 5, 6 ]
index = firstRepeatingElement(array,len(array))
if index != -1:
    print(f"First repeating element is: {array[index]}")
else:
    print("No repeating element.")

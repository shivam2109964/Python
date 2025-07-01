def largest(array, length):
    max = array[0]
    for i in range(1, length):
        if(array[i] > max):
            max = array[i]
    return max

length = int(input("Enter the length of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
largestElement = largest(array, length)
print(f"Largest element is: {largestElement}")
    
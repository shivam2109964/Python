length = int(input("Enter the length of array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]

def sum_of_element(arrayValue):
    sum = 0
    for i in range(len(arrayValue)):
        sum += arrayValue[i]
    return sum

result = sum_of_element(arrayValue= array)
print(f"The result is {result}")
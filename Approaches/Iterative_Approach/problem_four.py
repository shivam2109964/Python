length = int(input("Enter the length of an array: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
sum = 0
for i in range(length):
    sum += array[i]
print(f"Total Sum is {sum}")
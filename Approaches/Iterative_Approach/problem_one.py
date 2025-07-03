# Print Even Numbers from 1 to N
# Input: N = 10
# Output: 2 4 6 8 10

def evenNumbers(value):
    evenDigits = []
    for i in range(1, value + 1):
        if(i % 2 == 0):
            evenDigits.append(i)
    return evenDigits

value = int(input("Enter the n value: "))
evenResult = evenNumbers(value)
print(f"Even Numbers from 0 to {value} is {evenResult}")

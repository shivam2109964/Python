# Count Digits of a Number
# Input: num = 12345
# Output: 5

def countNumber(value):
    count = 0
    while(value != 0):
        value = value // 10
        count += 1
    return count 

value = int(input("Enter the number: "))
result = countNumber(value)
print(f"Total Digits is: {result}")

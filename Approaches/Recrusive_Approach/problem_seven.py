def sumOfDigits(number):
    if(number == 0):
        return 0
    return number % 10 + sumOfDigits(number // 10)

number = int(input("Enter the number: "))
result = sumOfDigits(number)
print(result)

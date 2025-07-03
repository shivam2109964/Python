def checkPrime(value):
    if(value <= 1):
        return False
    if(value == 2):
        return True
    if(value % 2 == 0):
        return False
    for i in range(3, int(value ** 0.5) + 1, 2):
        if(value % i == 0):
            return False
    return True
    

value = int(input("Enter the value to check its prime or not: "))
result = checkPrime(value)
if result == True:
    print(f"{value} is prime no.")
else:
    print(f"{value} is not a prime no.")


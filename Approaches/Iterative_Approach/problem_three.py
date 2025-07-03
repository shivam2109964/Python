def factorialValue(value):
    fact = 1
    for i in range(1, value + 1):
        fact *= i
    return fact

value = int(input("Enter the n value to cal fac: "))
result = factorialValue(value)
print(f"Factorial of {value} is {result}")

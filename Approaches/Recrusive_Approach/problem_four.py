def factorialValue(n):
    if(n == 1):
        return n
    return n * factorialValue(n - 1)

n = int(input("Enter the n value: "))
result = factorialValue(n)
print(result)

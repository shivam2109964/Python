def missing_number_by_linear_search(array):
    length = len(array) + 1
    for i in range(1, length - 1):
        found = False
        for j in range(0, length - 1):
            if array[j] == i:
                found = True
                break
        if found != True:
            return i
    return -1

def missing_number_by_hash(array):
    length = len(array) + 1
    # Create a hash array of size length + 1
    hash = [0] * (length + 1)
    # Store the frequencies of elements
    for i in range(length - 1):
        hash[array[i]] += 1
    # Find the missing number
    for i in range(1, length + 1):
        if hash[i] == 0:
            return i
    return -1

def missing_number_by_formula(array):
    length = len(array) + 1
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    expSum = length * (length + 1) // 2
    return expSum - sum

def missing_number_by_xor(array):
    length = len(array) + 1
    xor_1 = 0
    xor_2 = 0
    for i in range(length - 1):
        xor_2 ^= array[i]
    for i in range(1, length + 1):
        xor_1 ^= i
    return xor_1 ^ xor_2

array = [8, 2, 4, 5, 3, 7, 1]
result = missing_number_by_linear_search(array)
print(f"Missing Number by Linear Search: {result}")
result_by_hash = missing_number_by_hash(array)
print(f"Missing Number by Hash: {result_by_hash}")
result_by_formula = missing_number_by_formula(array)
print(f"Missing Number by Formula: {result_by_formula}")
result_by_xor = missing_number_by_xor(array)
print(f"Missing Number by XOR: {result_by_xor}")
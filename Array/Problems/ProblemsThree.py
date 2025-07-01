def getThreeLargest(array):
    first = second = third = float('-inf')
    for x in array:
        if x > first:
            third = second
            second = first
            first = x
        elif x > second and x != first:
            third = second
            second = x
        elif x > third and x != second and x != first:
            third = x
    res = []
    if first == float('-inf'):
        return res
    res.append(first)
    if second == float('-inf'):
        return res
    res.append(second)
    if third == float('-inf'):
        return res
    res.append(third)
    
    return res

def threeTraversal(array):
    length = len(array)
    largest = secondLargest = thirdLargest = float('-inf')
    res = []
    for i in range(length):
        if array[i] > largest:
            largest = array[i]
    if largest == float('-inf'):
        return res
    res.append(largest)
    
    for i in range(length):
        if array[i] > secondLargest and array[i] != largest:
            secondLargest = array[i]
    if secondLargest == float('-inf'):
        return res
    res.append(secondLargest)
    
    for i in range(length):
        if array[i] > thirdLargest and array[i] != secondLargest and array[i] != largest:
            thirdLargest = array[i]
    if thirdLargest == float('-inf'):
        return res
    res.append(thirdLargest)
    return res
        

array = [10, 9, 9]
res = getThreeLargest(array)
print(" ".join(map(str, res)))
resTrave = threeTraversal(array)
print(" ".join(map(str, resTrave)))

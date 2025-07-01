import bisect

array = [ 14, 26, 41, 2, 69, 85, 74, 13, 64, 45 ]
array.sort()
print(array)
target = 69
index = bisect.bisect_left(array, target)
if index < len(array) and array[index] == target:
    print(f"Found at index: {index}")
else:
    print('Not found')
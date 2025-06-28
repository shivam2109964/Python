def linearSearch(key, length, array):
    for i in range(0, length):
        if(array[i] == key):
            return i
        
    return -1

array = [8,2,7,1,6,3,64,81,73]
key = 81
result = linearSearch(key, len(array), array)

if(result != -1):
    print(f"Match found at index: {result}")
else:
    print("Match not found")


        
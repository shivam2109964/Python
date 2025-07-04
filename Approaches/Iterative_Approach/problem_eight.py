def freqCount(strValue, char):
    count = 0
    for i in range(len(strValue)):
        if strValue[i] == char:
            count += 1
    return count

strValue = input("Enter the string value: ")
char = input("Enter the char: ")[0]
result = freqCount(strValue, char)
print(f"In the String: {strValue} the freq of char: {char} is {result}")

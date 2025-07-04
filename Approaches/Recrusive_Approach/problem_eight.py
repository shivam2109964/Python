def reverseString(strValue, index):
    if(index < 0):
        return 0
    print(strValue[index], end="")
    reverseString(strValue, index - 1)
    

strValue = input("Enter the string value: ")
reverseString(strValue, len(strValue) - 1)
strValue = input("Enter the String value: ")
reversedStr = ""
for i in range(len(strValue) -1, -1, -1):
    reversedStr += strValue[i]
print(f"Reverse String: {reversedStr}")
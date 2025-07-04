def checkPalindrome(strValue, start, end):
    if(start >= end):
        return True

    if(strValue[start] != strValue[end]):
        return False
    return checkPalindrome(strValue, start + 1, end - 1)

strValue = input("Enter the String value: ")
result = checkPalindrome(strValue, 0, len(strValue) - 1)
if result:
    print("It's Palindrome")
else: 
    print("It's not a Palindrome")


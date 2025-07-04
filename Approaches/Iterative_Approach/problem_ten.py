def checkPalindrome(array, length):
    isPalindrome = True
    for i in range(0, (length // 2 + 1 and length != 1)):
        if(array[i] != array[length - 1 - i]):
            isPalindrome = False
            break
    return isPalindrome
         

length = int(input("Enter the length: "))
array = [int(input(f"Enter the {i + 1} element: ")) for i in range(length)]
result = checkPalindrome(array, length)
if(result == True):
    print("Its Palindrome")
else:
    print("Its not a Palindrome")
